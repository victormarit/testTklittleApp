import mysql.connector

class DB : 
    def __init__(self):
        self.connection = ''
        self.cursor = ''
        self.host = 'localhost'
        self.db = 'testcollecdb1'
        self.user = 'root'
        self.password = ''
        self.port = '3308'

    def connectionDB(self): 
        try : 
            self.connection = mysql.connector.connect(host = self.host, database = self.db, user = self.user, password = self.password, port = self.port)
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            print(err)



