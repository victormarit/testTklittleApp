import sys
sys.path.append('..')
import unittest
from classes.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.infos = (1,'','','','',False)
        self.testUser = User(self.infos) 
    
    def test_User_IsInstance(self):
        self.assertIsInstance(self.testUser, User)

if __name__ == '__main__' : 
    unittest.main()