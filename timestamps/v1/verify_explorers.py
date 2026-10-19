from pathlib import Path
import json,hashlib,urllib.request,datetime
from opentimestamps.core.timestamp import DetachedTimestampFile
from opentimestamps.core.serialize import BytesDeserializationContext
from opentimestamps.core.notary import BitcoinBlockHeaderAttestation
p=Path('outputs/Hall_v1_bitcoin_timestamp')
def get(url):
 with urllib.request.urlopen(url,timeout=20) as r:return r.read().decode()
records=[]
for name in ['Hall-Polynomial-Conjecture-v1.pdf','Hall-Polynomial-Conjecture-v1-source.zip']:
 proof=DetachedTimestampFile.deserialize(BytesDeserializationContext((p/(name+'.ots')).read_bytes()))
 assert hashlib.sha256((p/name).read_bytes()).digest()==proof.file_digest
 attest=sorted([(a.height,msg) for msg,a in proof.timestamp.all_attestations() if isinstance(a,BitcoinBlockHeaderAttestation)])
 height,msg=attest[0]
 blockhash=get(f'https://blockstream.info/api/block-height/{height}').strip()
 block=json.loads(get('https://blockstream.info/api/block/'+blockhash))
 assert msg[::-1].hex()==block['merkle_root']
 raw=bytes.fromhex(get('https://blockstream.info/api/block/'+blockhash+'/header').strip())
 assert raw[36:68]==msg
 assert hashlib.sha256(hashlib.sha256(raw).digest()).digest()[::-1].hex()==blockhash
 records.append(dict(file=name,sha256=proof.file_digest.hex(),block_height=height,block_hash=blockhash,block_time_utc=datetime.datetime.fromtimestamp(block['timestamp'],datetime.timezone.utc).isoformat(),block_time_beijing=datetime.datetime.fromtimestamp(block['timestamp'],datetime.timezone(datetime.timedelta(hours=8))).isoformat(),verification='Original digest, OTS operation path, block Merkle root, header hash checked; block header obtained from Blockstream. Public explorer verification, not local Bitcoin full-node consensus verification.'))
 print(json.dumps(records[-1]),flush=True)
(p/'verification.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
