from pathlib import Path
import hashlib,json,os,datetime,concurrent.futures
from opentimestamps.core.timestamp import DetachedTimestampFile
from opentimestamps.core.op import OpSHA256,OpAppend
from opentimestamps.core.serialize import StreamSerializationContext,BytesDeserializationContext
from opentimestamps.calendar import RemoteCalendar
from opentimestamps.core.notary import BitcoinBlockHeaderAttestation,PendingAttestation
HERE=Path(__file__).resolve().parent
ORIGINAL=HERE.parents[2]/'assets'
CALENDARS=['https://a.pool.opentimestamps.org','https://b.pool.opentimestamps.org','https://a.pool.eternitywall.com']
FILES=['Hall-Polynomial-Conjecture-v2.pdf','Hall-Polynomial-Conjecture-v2-complete.zip']
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(proof,path):
    with path.open('wb') as out:proof.serialize(StreamSerializationContext(out))
def load(path):return DetachedTimestampFile.deserialize(BytesDeserializationContext(path.read_bytes()))
def submit_one(url,msg):
    try:return url,RemoteCalendar(url).submit(msg,timeout=15),None
    except Exception as e:return url,None,str(e)
def nodes(root):
    yield root
    for child in root.ops.values():
        yield from nodes(child)
def run():
    receipt={'updated_utc':utc(),'files':[],'verification':'Proof parsing and original-file SHA-256 checked. A pending calendar attestation is not Bitcoin confirmation.'}
    for name in FILES:
        target=HERE/name
        source=(ORIGINAL/name) if (ORIGINAL/name).exists() else target
        if not target.exists():target.write_bytes(source.read_bytes())
        assert target.read_bytes()==source.read_bytes()
        path=HERE/(name+'.ots')
        errors=[]
        if not path.exists():
            with target.open('rb') as f:proof=DetachedTimestampFile.from_fd(OpSHA256(),f)
            nonce=proof.timestamp.ops.add(OpAppend(os.urandom(16)))
            tip=nonce.ops.add(OpSHA256())
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
                results=list(pool.map(lambda u:submit_one(u,tip.msg),CALENDARS))
            success=0
            for url,stamp,error in results:
                if stamp is not None:tip.merge(stamp);success+=1
                else:errors.append({'calendar':url,'error':error})
            if success==0:raise RuntimeError('No calendar accepted commitment: '+str(errors))
            save(proof,path)
        proof=load(path)
        pending=[(msg,a) for msg,a in proof.timestamp.all_attestations() if isinstance(a,PendingAttestation)]
        for msg,a in pending:
            url=a.uri.decode() if isinstance(a.uri,bytes) else a.uri
            try:
                newer=RemoteCalendar(url).get_timestamp(msg,timeout=10)
                for node in list(nodes(proof.timestamp)):
                    if node.msg==msg:node.merge(newer)
            except Exception as e:errors.append({'calendar':url,'upgrade_error':str(e)})
        save(proof,path)
        checked=load(path)
        digest=hashlib.sha256(target.read_bytes()).digest()
        assert checked.file_digest==digest
        blocks=[a.height for _,a in checked.timestamp.all_attestations() if isinstance(a,BitcoinBlockHeaderAttestation)]
        record={'file':name,'sha256':digest.hex(),'proof':path.name,'proof_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'bitcoin_block_heights':blocks,'status':'bitcoin_attestation_present_not_yet_independently_verified' if blocks else 'pending_bitcoin_confirmation','errors':errors}
        receipt['files'].append(record)
        print(name,record['status'],blocks,flush=True)
    (HERE/'status.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
if __name__=='__main__':run()

