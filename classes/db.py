import mysql.connector

class DB : 
    def __init__(self):
        self.conn = ''
        self.cursor = ''

    def connectionBD(self) :
        try : 
            self.conn = mysql.connector.connect(host = 'localhost', database = 'testcollecdb1', user = 'root', password = '', port = '3308')
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err: 
            print(err)

    def login(self, log):
        req = 'SELECT * FROM user WHERE email = %s AND pw = %s'
        try : 
            self.connectionBD()
            self.cursor.execute(req, log)
            data = self.cursor.fetchone()
        except : 
            print('Pas d\'utilisateur trouvé')
        finally:
            try : 
                if self.conn.is_connected():
                    self.conn.close()
                    if data is None :
                        return []
                    else :
                        return data
            except: 
                return
    
    def testEmail(self, email):
        test = (email,)
        req = 'SELECT * FROM user WHERE email= %s'
        try:
            self.connectionBD()
            self.cursor.execute(req, test)
            data = self.cursor.fetchone()
        except : 
            print('Err')
        finally : 
            try : 
                if self.conn.is_connected():
                    self.conn.close()
                    if data is None :
                        return True
                    else :
                        return False
            except: 
                return 

    def subscribe(self, info):
        req = 'INSERT INTO user (nom, prenom, email, pw) VALUES (%s,%s,%s,%s)'
        try:
            self.connectionBD()
            self.cursor.execute(req, info)
            self.conn.commit()
        except:
            print('\n\n\nEchec de l\'ajout de l\'utilisateur')
        finally:
            try:
                if self.conn.is_connected():
                    self.conn.close()
            except:
                pass

    def deleteUser(self, info):
        req = 'DELETE FROM user WHERE user.nom = %s AND user.prenom = %s AND user.email = %s AND user.pw = %s'
        try :
            self.connectionBD()
            self.cursor.execute(req, info)
            self.conn.commit()
        except :
            print('Fail to delete user') 
        finally:
            try:
                if self.conn.is_connected():
                    self.conn.close()
            except:
                pass

    def findGenres(self):
        req = 'SELECT * FROM genre'
        try :
            self.connectionBD()
            self.cursor.execute(req)
            data = self.cursor.fetchall()
        except :
            print('Fail to find Genre') 
        finally:
            try:
                if self.conn.is_connected():
                    self.conn.close()
                    if data is None :
                        return []
                    else :
                        return data
            except:
                return
    
    def addNewGenre(self, info):
        req = 'INSERT INTO genre (nomGenre) VALUES(%s);'
        try:
            self.connectionBD()
            self.cursor.execute(req, info)
            self.conn.commit()
        except:
            print('\n\n\nEchec de l\'ajout du genre')
        finally:
            try:
                if self.conn.is_connected():
                    self.conn.close()
            except:
                pass

    def deleteOldGenre(self, info):
        req = 'DELETE FROM genre WHERE genre.nomGenre = %s;'
        try :
            self.connectionBD()
            self.cursor.execute(req, info)
            self.conn.commit()
        except :
            print('Fail to delete genre') 
        finally:
            try:
                if self.conn.is_connected():
                    self.conn.close()
            except:
                pass
        