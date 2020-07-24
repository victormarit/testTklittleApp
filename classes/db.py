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

#About User
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

    def updateUser(self, info):
        req = 'UPDATE user SET user.nom = %s, user.prenom = %s, user.email = %s WHERE user.idUser = %s'
        try :
            self.connectionBD()
            self.cursor.execute(req, info)
            self.conn.commit()
        except :
            print('Fail to update user') 
        finally:
            try:
                if self.conn.is_connected():
                    self.conn.close()
            except:
                pass
    
    def updateUserPasswordDB(self, info):
        req = 'UPDATE user SET user.pw = %s WHERE user.idUser = %s'
        try :
            self.connectionBD()
            self.cursor.execute(req, info)
            self.conn.commit()
        except :
            print('Fail to update password') 
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

#About Genre
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
    
    def findGenre(self, info):
        req = 'SELECT * FROM genre WHERE genre.nomGenre = %s'
        try :
            self.connectionBD()
            self.cursor.execute(req, info)
            data = self.cursor.fetchone()
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

    def updateGenre(self, info):
        req = 'UPDATE genre SET genre.nomGenre = %s WHERE genre.idGenre = %s'
        try :
            self.connectionBD()
            self.cursor.execute(req, info)
            self.conn.commit()
        except :
            print('Fail to update genre') 
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

#About Console
    def findConsoles(self):
        req = 'SELECT * FROM console'
        try :
            self.connectionBD()
            self.cursor.execute(req)
            data = self.cursor.fetchall()
        except :
            print('Fail to find Console') 
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

    def findConsole(self, info):
        req = 'SELECT * FROM console WHERE console.Nom = %s'
        try :
            self.connectionBD()
            self.cursor.execute(req, info)
            data = self.cursor.fetchone()
        except :
            print('Fail to find Console') 
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
    def addNewConsole(self, info):
        req = 'INSERT INTO console (Nom, Constructeur, logo, annee) VALUES(%s, %s, %s, %s);'
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
    def updateConsole(self, info):
        req = 'UPDATE console SET console.Nom = %s, console.Constructeur = %s, console.logo = %s, console.annee = %s WHERE console.idConsole = %s'
        try :
            self.connectionBD()
            self.cursor.execute(req, info)
            self.conn.commit()
        except :
            print('Fail to update console') 
        finally:
            try:
                if self.conn.is_connected():
                    self.conn.close()
            except:
                pass
            
    def deleteOldConsole(self, info):
        req = 'DELETE FROM console WHERE console.Nom = %s;'
        try :
            self.connectionBD()
            self.cursor.execute(req, info)
            self.conn.commit()
        except :
            print('Fail to delete console') 
        finally:
            try:
                if self.conn.is_connected():
                    self.conn.close()
            except:
                pass

#Collection 
    def userConsoleCollection(self, info):
        req = 'SELECT console.Nom, possessionconsole.nb FROM possessionconsole, console WHERE possessionconsole.idUser = %s AND console.idConsole = possessionconsole.idConsole'
        try : 
            self.connectionBD()
            self.cursor.execute(req, info)
            data = self.cursor.fetchall()
        except : 
            print('Pas de console trouvée')
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

    def userConsoleCollectionQauntity(self, info):
        req = 'SELECT possessionconsole.nb FROM possessionconsole, console WHERE possessionconsole.idUser = %s AND console.idConsole = possessionconsole.idConsole AND console.Nom = %s'
        try : 
            self.connectionBD()
            self.cursor.execute(req, info)
            data = self.cursor.fetchone()
        except : 
            print('Pas de console trouvée')
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
    
    def insertConsoleUser(self, info):
        req = 'INSERT INTO possessionconsole (idUser, idConsole, nb) VALUES (%s, %s, %s);'
        try :
            self.connectionBD()
            self.cursor.execute(req, info)
            self.conn.commit()
        except :
            print('Fail to add console') 
        finally:
            try:
                if self.conn.is_connected():
                    self.conn.close()
            except:
                pass

    def updateConsoleUser(self, info):
        req = 'UPDATE possessionconsole SET possessionconsole.nb = %s WHERE possessionconsole.idConsole = %s AND possessionconsole.idUser = %s'
        try :
            self.connectionBD()
            self.cursor.execute(req, info)
            self.conn.commit()
        except :
            print('Fail to add console') 
        finally:
            try:
                if self.conn.is_connected():
                    self.conn.close()
            except:
                pass

    def deleteConsoleUser(self, info):
        req = 'DELETE FROM possessionconsole WHERE possessionconsole.idUser = %s AND possessionconsole.idConsole = %s'
        try :
            self.connectionBD()
            self.cursor.execute(req, info)
            self.conn.commit()
        except :
            print('Fail to add console') 
        finally:
            try:
                if self.conn.is_connected():
                    self.conn.close()
            except:
                pass