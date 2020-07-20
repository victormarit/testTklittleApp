import sys
sys.path.append('..')
import unittest
from fonctions.fonctionsTk import hashPassword

class TestFonctionTk(unittest.TestCase):
    def setUp(self):
        self.mp = 'mpTest'
    
    def test_fonctionTK_hashPassword(self):
        password = hashPassword(self.mp)
        self.assertEqual(len(password), 40)

if __name__ == '__main__' : 
    unittest.main()
