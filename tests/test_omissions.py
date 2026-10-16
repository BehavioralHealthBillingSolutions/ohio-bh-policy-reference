import copy
import hashlib
import importlib.util
from pathlib import Path
import unittest

path=Path(__file__).resolve().parents[1]/'.github/scripts/validate_publication.py'
spec=importlib.util.spec_from_file_location('guard',path);guard=importlib.util.module_from_spec(spec);spec.loader.exec_module(guard)


class OmissionTests(unittest.TestCase):
    def setUp(self):
        self.text=('INCOMPLETE REFERENCE EXCERPT\nhttps://example.invalid/original.pdf\n'
                   '## Original PDF page 1\nretained\n## OMITTED — original PDF pages 2–3\n'
                   '## Original PDF page 4\nretained\n').encode()
        self.record=dict(id='example',pages=4,omit=[2,3],included_pdf_pages=[1,4],omitted_pdf_pages=[2,3],
                         excerpt_path='example.md',excerpt_sha256=hashlib.sha256(self.text).hexdigest(),
                         url='https://example.invalid/original.pdf',completeness_claim=False)

    def check(self,record=None,text=None):
        return guard.check_omissions([record or self.record],lambda _:self.text if text is None else text)

    def test_valid_omission_inventory(self):self.assertEqual([],self.check())

    def test_missing_original_page_rejected(self):
        r=copy.deepcopy(self.record);r['included_pdf_pages']=[1]
        self.assertTrue(any('gaps' in e for e in self.check(r)))

    def test_excluded_page_in_excerpt_rejected(self):
        r=copy.deepcopy(self.record);r['included_pdf_pages']=[1,2,4]
        self.assertTrue(any('overlap' in e for e in self.check(r)))

    def test_completeness_claim_rejected(self):
        r=copy.deepcopy(self.record);r['completeness_claim']=True
        self.assertTrue(any('disclosure' in e for e in self.check(r)))

    def test_modified_excerpt_rejected(self):
        self.assertTrue(any('hash mismatch' in e for e in self.check(text=self.text+b'changed')))

    def test_omission_marker_required(self):
        t=self.text.replace('## OMITTED — original PDF pages 2–3'.encode(),b'missing')
        self.assertTrue(any('omission marker' in e for e in self.check(text=t)))

    def test_page_heading_inventory_required(self):
        self.assertTrue(any('headings' in e for e in self.check(text=self.text.replace(b'## Original PDF page 4',b'## Original PDF page 3'))))


if __name__=='__main__':unittest.main()
