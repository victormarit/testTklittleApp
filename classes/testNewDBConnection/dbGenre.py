from classes.testNewDBConnection.db import DB

class DbGenre(DB):
    def __init__(self):
        DB.__init__(self)

    def findAllGenres(self):
        '''
        to get all kind of genres
        return :
        -[(idGenre', 'nameGenre'),] 
        -[]
        -void
        '''
        req = 'SELECT * FROM genre'
        try :
            self.connectionDB()
            self.cursor.execute(req)
            data = self.cursor.fetchall()
        except :
            print('Fail to find Genre') 
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
    
    def findOneGenre(self, info):
        '''
        to find a specific genre in DB
        params :
        -info : ('genreName',)
        return :
        -[(idGenre', 'nameGenre'),] 
        -[]
        -void
        '''
        req = 'SELECT * FROM genre WHERE genre.nomGenre = %s'
        try :
            self.connectionDB()
            self.cursor.execute(req, info)
            data = self.cursor.fetchone()
        except :
            print('Fail to find Genre') 
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
    
    def findGenreWithId(self, id):
        '''
        to find a specific genre in DB
        params :
        -info : ('genreName',)
        return :
        -[('nameGenre',),] 
        -[]
        -void 
        '''
        req = 'SELECT genre.nomGenre FROM genre WHERE genre.idGenre = %s'
        try :
            self.connectionDB()
            self.cursor.execute(req, id)
            data = self.cursor.fetchone()
        except :
            print('Fail to find Genre') 
        finally:
            try:
                if self.connection.is_connected():
                    self.connection.close()
                    if data is None :
                        return []
                    else :
                        return data[0]
            except:
                return

    def addNewGenre(self, info):
        '''
        to add a genre in DB
        params 
        -info : ('genreName')
        '''
        req = 'INSERT INTO genre (nomGenre) VALUES(%s);'
        try:
            self.connectionDB()
            self.cursor.execute(req, info)
            self.connection.commit()
        except:
            print('\n\n\nEchec de l\'ajout du genre')
        finally:
            try:
                if self.connection.is_connected():
                    self.connection.close()
            except:
                pass

    def updateGenre(self, info):
        '''
        to update genre name
        params : 
        -info : ('genreName', 'idGenre')
        '''
        req = 'UPDATE genre SET genre.nomGenre = %s WHERE genre.idGenre = %s'
        try :
            self.connectionDB()
            self.cursor.execute(req, info)
            self.connection.commit()
        except :
            print('Fail to update genre') 
        finally:
            try:
                if self.connection.is_connected():
                    self.connection.close()
            except:
                pass

    def deleteOldGenre(self, info):
        '''
        to delete genre in DB
        params : 
        info : ('genreName',)
        '''
        req = 'DELETE FROM genre WHERE genre.nomGenre = %s;'
        try :
            self.connectionDB()
            self.cursor.execute(req, info)
            self.connection.commit()
        except :
            print('Fail to delete genre') 
        finally:
            try:
                if self.connection.is_connected():
                    self.connection.close()
            except:
                pass