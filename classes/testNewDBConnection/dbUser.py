from db import DB

class DbUser(DB):
    def __init__(self):
        DB.__init__(self)

    def testEmail(self, email):
        '''
        to test if an email is already in the DB
        Param : 
        -email, tuple, string
        Retun : 
        -already in DB : return false
        -Not in DB : return True
        -Fail to connect to DB : return nothing
        '''
        req = 'SELECT * FROM user WHERE email= %s'
        try:
            self.connectionDB()
            self.cursor.execute(req, email)
            data = self.cursor.fetchone()
        except : 
            print('Err')
        finally : 
            try : 
                if self.connection.is_connected():
                    self.connection.close()
                    if data is None :
                        return True
                    else :
                        return False
            except: 
                return 

    def subscribe(self, info):
        '''
        To register an user in DB
        param : info 
        -info : tuple ('name','lastname', 'email', 'password')
        '''
        req = 'INSERT INTO user (nom, prenom, email, pw) VALUES (%s,%s,%s,%s)'
        try:
            self.connectionDB()
            self.cursor.execute(req, info)
            self.connection.commit()
        except:
            print('\n\n\nEchec de l\'ajout de l\'utilisateur')
        finally:
            try:
                if self.connection.is_connected():
                    self.connection.close()
            except:
                pass

    def login(self, log):
        '''
        To log an user, check email and password 
        Param : 
        -log : tuple with 2 string ('email', 'password')
        Return :
        -Found : return user information [id, lastname, firstname, email, password, admin]
        -Not in DB : return []
        -Fail to connect to DB : return nothing
        '''
        req = 'SELECT * FROM user WHERE email = %s AND pw = %s'
        try : 
            self.connectionDB()
            self.cursor.execute(req, log)
            data = self.cursor.fetchone()
        except : 
            print('Pas d\'utilisateur trouvé')
        finally:
            try : 
                if self.connection.is_connected():
                    self.connection.close()
                    if data is None :
                        return []
                    else :
                        return data
            except: 
                return

    def updateUser(self, info):
        '''
        to update user informations 
        params : 
        -infos : tuple ('name', 'firstname', 'email', 'id')
        '''
        req = 'UPDATE user SET user.nom = %s, user.prenom = %s, user.email = %s WHERE user.idUser = %s'
        try :
            self.connectionDB()
            self.cursor.execute(req, info)
            self.connection.commit()
        except :
            print('Fail to update user') 
        finally:
            try:
                if self.connection.is_connected():
                    self.connection.close()
            except:
                pass

    def updateUserPasswordDB(self, info):
            '''
        to update user password 
        params : 
        -infos : tuple ('password', 'id')
        '''
        req = 'UPDATE user SET user.pw = %s WHERE user.idUser = %s'
        try :
            self.connectionDB()
            self.cursor.execute(req, info)
            self.connection.commit()
        except :
            print('Fail to update password') 
        finally:
            try:
                if self.connection.is_connected():
                    self.connection.close()
            except:
                pass

    def deleteUser(self, info):
        '''
        to delete an user account
        params :
        -info : tuple ('name','firstname','email','password')
        '''
        req = 'DELETE FROM user WHERE user.nom = %s AND user.prenom = %s AND user.email = %s AND user.pw = %s'
        try :
            self.connectionDB()
            self.cursor.execute(req, info)
            self.connection.commit()
        except :
            print('Fail to delete user') 
        finally:
            try:
                if self.connection.is_connected():
                    self.connection.close()
            except:
                pass