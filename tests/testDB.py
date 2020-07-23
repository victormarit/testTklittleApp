import sys
sys.path.append('..')
import unittest
from classes.db import DB

class TestDB(unittest.TestCase): 
    def setUp(self):
        self.dbTest = DB()
        self.infosUser = ('fakeUser', 'fakeName', 'fakeEmail@fake.com', 'adminadmin')
        self.logUser = ('fakeEmail@fake.com', 'adminadmin')
        self.genre = ('testGenre',)
        self.console = ('testConsole', 'fakeConstructeur', 'fakePathForLogo', '2020')

    def test_DB_DbIsInstance(self):
        self.assertIsInstance(self.dbTest, DB)

    def test_connectionDB_dbisConnect(self):
        self.dbTest.connectionBD()
        self.assertIsNot(self.dbTest.conn, '')

    def test_login_TrueArguments(self):
        user = ('victormarit.95@gmail.com', 'cc6511246b39e5cca492c3f945cdebe4fcea0052')
        data = self.dbTest.login(user)
        self.assertIsNotNone(data)
        self.assertEqual(len(data), 6)

    def test_login_FalseArguments(self):
        user = ('victormarit', 'lfngldk')
        data = self.dbTest.login(user)
        self.assertEqual(len(data),0)

    def test_testEmail_EmailInDB(self):
        email = 'test123456789.95@gmail.com'
        data = self.dbTest.testEmail(email)
        self.assertTrue(data)
    
    def test_testEmail_EmailNotInDB(self):
        email = 'victormarit.95@gmail.com'
        data = self.dbTest.testEmail(email)
        self.assertFalse(data)

    def test_subscribe_delete_user(self):
        #Create and test user
        self.dbTest.subscribe(self.infosUser)
        data = self.dbTest.login(self.logUser)
        self.assertEqual(len(data), 6)
        #delete and test user
        self.dbTest.deleteUser(self.infosUser)
        data = self.dbTest.login(self.logUser)
        self.assertEqual(len(data), 0)

    def test_findGenres(self):
        data = self.dbTest.findGenres()
        self.assertTrue(len(data)>=0)
    
    def test_createGenre_deleteGenre(self):
        #Create and test genre
        self.dbTest.addNewGenre(self.genre)
        data = self.dbTest.findGenre(self.genre)
        self.assertEqual(len(data), 2)
        #delete and test genre
        self.dbTest.deleteOldGenre(self.genre)
        data = self.dbTest.findGenre(self.genre)
        self.assertEqual(len(data), 0)

    def test_createConsole_deleteConsole(self):
        info = (self.console[0],)
        #Create console and find console on DB
        self.dbTest.addNewConsole(self.console)
        data = self.dbTest.findConsole(info)
        self.assertEqual(len(data), 5)
        #updtate console 
        consoleBis = ('testConsoleBis', 'fakeConstructeur', 'fakePathForLogo', '2020', data[0])
        self.dbTest.updateConsole(consoleBis)
        consoleThird = ('testConsoleBis',)
        data = self.dbTest.findConsole(consoleThird)
        print(data)
        self.assertEqual(len(data[1]), 14)
        #Delete Console and try to find result on DB
        self.dbTest.deleteOldConsole(consoleThird)
        data = self.dbTest.findConsole(consoleThird)
        self.assertEqual(len(data), 0)


if __name__ == '__main__' : 
    unittest.main()
