from db import DB

class DbConsoleCollection(DB):
    def __init__(self):
        DB.__init__(self)

    def userConsoleCollection(self, info):
        '''
        to get user console collection
        params :
        -info : ('idUser',)
        return
        -[('consoleName', 'consoleQuantity'),]
        -[]
        -void
        '''
        req = 'SELECT console.Nom, possessionconsole.nb FROM possessionconsole, console WHERE possessionconsole.idUser = %s AND console.idConsole = possessionconsole.idConsole'
        try : 
            self.connectionDB()
            self.cursor.execute(req, info)
            data = self.cursor.fetchall()
        except : 
            print('Pas de console trouvée')
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
    
    def insertConsoleUser(self, info):
        '''
        to add console collection in DB
        params :
        -info : ('idUser', 'idConsole', nb)
        '''
        req = 'INSERT INTO possessionconsole (idUser, idConsole, nb) VALUES (%s, %s, %s);'
        try :
            self.connectionDB()
            self.cursor.execute(req, info)
            self.connection.commit()
        except :
            print('Fail to add console') 
        finally:
            try:
                if self.connection.is_connected():
                    self.connection.close()
            except:
                pass

    def updateConsoleUser(self, info):
        '''
        to update console collection in DB
        params :
        -info : (possessionConsoleQuantity, 'idConsole', 'idUser')
        '''
        req = 'UPDATE possessionconsole SET possessionconsole.nb = %s WHERE possessionconsole.idConsole = %s AND possessionconsole.idUser = %s'
        try :
            self.connectionDB()
            self.cursor.execute(req, info)
            self.connection.commit()
        except :
            print('Fail to update console possession') 
        finally:
            try:
                if self.connection.is_connected():
                    self.connection.close()
            except:
                pass

    def deleteConsoleUser(self, info):
        '''
        to delete a console
        param :
        -info : ('idUser', 'idConsole')
        '''
        req = 'DELETE FROM possessionconsole WHERE possessionconsole.idUser = %s AND possessionconsole.idConsole = %s'
        try :
            self.connectionDB()
            self.cursor.execute(req, info)
            self.connection.commit()
        except :
            print('Fail to add console') 
        finally:
            try:
                if self.connection.is_connected():
                    self.connection.close()
            except:
                pass

