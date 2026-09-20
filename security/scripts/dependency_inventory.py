from pathlib import Path
import json,sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '.')
out=[]
p=root/'package.json'
if p.exists():
 d=json.loads(p.read_text(encoding='utf-8'))
 for scope in ('dependencies','devDependencies'):
  for name,ver in d.get(scope,{}).items(): out.append({'ecosystem':'npm','name':name,'version':ver,'scope':scope})
r=root/'requirements.txt'
if r.exists():
 for line in r.read_text().splitlines():
  line=line.strip()
  if line and not line.startswith('#'): out.append({'ecosystem':'python','requirement':line})
print(json.dumps(out,ensure_ascii=False,indent=2))
