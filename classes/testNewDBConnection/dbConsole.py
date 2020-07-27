from db import DB

class DbConsole(DB):
    def __init__(self):
        DB.__init__(self)

    def findAllConsoles(self):
        '''
        to find all consoles in DB
        return 
        -If they are some console in DB : list ['id' , 'consoleName', 'builderCompany', 'logoPath', 'releaseYear']
        -If thez are no console in DB : return a void list
        -If connection failure : void return
        '''
        req = 'SELECT * FROM console'
        try :
            self.connectionDB()
            self.cursor.execute(req)
            data = self.cursor.fetchall()
        except :
            print('Fail to find Consoles') 
        finally:
            try:
                if self.connection.is_connected():
                    self.connection.close()
                    if data is None :
                        return []
                    else :
                        return data
            except:
                return

    def findOneConsole(self, info):
        '''
        to find one console in the DB
        param :
        -info : tuple ('console.nom',)
        return :
        -if counsole found : ('id', 'consoleName', 'consoleBuilder', 'logoPath', 'releaseYear')
        '''
        req = 'SELECT * FROM console WHERE console.Nom = %s'
        try :
            self.connectionDB()
            self.cursor.execute(req, info)
            data = self.cursor.fetchone()
        except :
            print('Fail to find Console') 
        finally:
            try:
                if self.connection.is_connected():
                    self.connection.close()
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


db = DbConsole()
print(db.findOneConsole(('PS4',)))