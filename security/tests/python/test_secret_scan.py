import tempfile,unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'scripts'))
from secret_scan import scan
class T(unittest.TestCase):
 def test_detect(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d); (p/'x.txt').write_text('ghp_'+'A'*30); self.assertTrue(scan(p))
 def test_clean(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d); (p/'x.txt').write_text('no secret'); self.assertFalse(scan(p))
if __name__=='__main__':unittest.main()
