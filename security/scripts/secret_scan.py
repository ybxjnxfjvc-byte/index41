from pathlib import Path
import re,sys
PATS={'private_key':re.compile(r'-----BEGIN .*PRIVATE KEY-----'),'github':re.compile(r'gh[pousr]_[A-Za-z0-9_]{20,}'),'aws':re.compile(r'AKIA[0-9A-Z]{16}'),'bearer':re.compile(r'Bearer\s+[A-Za-z0-9._-]{24,}',re.I)}
def scan(root):
 hits=[]
 for p in Path(root).rglob('*'):
  if not p.is_file() or any(x in p.parts for x in ('.git','node_modules')):continue
  if p.name=='.env.example':continue
  if p.suffix.lower() not in {'.md','.py','.js','.json','.yml','.yaml','.txt','.html'}:continue
  t=p.read_text(encoding='utf-8',errors='ignore')
  for name,rx in PATS.items():
   if rx.search(t):hits.append((str(p),name))
 return hits
if __name__=='__main__':
 h=scan(sys.argv[1] if len(sys.argv)>1 else '.'); print('PASS' if not h else 'FAIL'); [print(*x) for x in h]; raise SystemExit(bool(h))
