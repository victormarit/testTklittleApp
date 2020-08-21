from classes.testNewDBConnection.db import DB

class DbGame(DB):
    def __init__(self):
        DB.__init__(self)

    def getAllGames(self):
        '''
        to find all consoles in DB
        return 
        -If they are some console in DB : list [(,),]
        -If thez are no console in DB : return a void list
        -If connection failure : void return
        '''
        req = 'SELECT * FROM jeu'
        try:
            self.connectionDB()
            self.cursor.execute(req)
            data = self.cursor.fetchall()
        except :
            print('Fail to find game')
        finally:
            if self.connection.is_connected():
                self.connection.close()
                if len(data) > 0 :
                    return data
                else: 
                    return []
            else:
                return 
    
    def getGameSearch(self, info):
        '''
        to get a list agame in function of a search 
        params 
        info = nameGame
        return 
        data [(,),]
        '''
        req = f'SELECT * FROM jeu WHERE jeu.Nom LIKE "%{info}%"'
        try:
            self.connectionDB()
            self.cursor.execute(req)
            data = self.cursor.fetchall()
        except :
            print('Fail to find game')
        finally:
            if self.connection.is_connected():
                self.connection.close()
                if len(data) > 0 :
                    return data
                else: 
                    return []
            else:
                return 

    def getUserGames(self, idUser):
        '''
        to find all user games 
        -params 
        idUser : (int,)
        -return 
        If they are some game in DB : list [(,),]
        If thez are no game in DB : return a void list
        If connection failure : void return
        '''
        req = 'SELECT * FROM gamecollection WHERE idUser = %s'
        try:
            self.connectionDB()
            self.cursor.execute(req, idUser)
            data = self.cursor.fetchall()
        except :
            print('Fail to find game(s)')
        finally:
            if self.connection.is_connected():
                self.connection.close()
                if data is None :
                    return []
                else: 
                    return data
            else:
                return 
        
    def addGameInDB(self, info):
        '''
        to a game in DB
        -params 
        info = (gameName, consoleID, genreId, pegi)
        '''
        req = 'INSERT INTO jeu (Nom, idConsole, pegi, idGenre) VALUES (%s, %s, %s, %s)'
        try:
            self.connectionDB()
            self.cursor.execute(req, info)
            self.connection.commit()
        except:
            print('Fail to add game in database')
        finally: 
            if self.connection.is_connected():
                self.connection.close()

    def addGameCollection(self, info):
        '''
        to add game in user collection
        params :
        -info = (idUser, idGame, nombre)
        '''
        req = 'INSERT INTO gamecollection (idUser, idJeu, nb) VALUES (%s, %s, %s)'
        try:
            self.connectionDB()
            self.cursor.execute(req, info)
            self.connection.commit()
        except:
            print('Fail to add game in user collection')
        finally: 
            if self.connection.is_connected():
                self.connection.close()

    def getGameId(self, info):
        '''
        to get game id
        params :
        -info = (gameName,)
        '''
        req = 'SELECT idJeu FROM jeu WHERE jeu.Nom = %s '
        try:
            self.connectionDB()
            self.cursor.execute(req, info)
            data = self.cursor.fetchone()
        except:
            print('Fail to get game id')
        finally: 
            if self.connection.is_connected():
                self.connection.close()
                if len(data) > 0 :
                    return data
                else: 
                    return []
            else:
                return 

    def getGameName(self, info):
        '''
        to get game name
        params :
        -info = (gameId,)
        '''
        req = 'SELECT Nom FROM jeu WHERE jeu.idJeu = %s '
        try:
            self.connectionDB()
            self.cursor.execute(req, info)
            data = self.cursor.fetchone()
        except:
            print('Fail to get game name')
        finally: 
            if self.connection.is_connected():
                self.connection.close()
                if len(data) > 0 :
                    return data
                else: 
                    return []
            else:
                return 

    def delAllGameCollection(self, info):
        '''
        to delete all user collection
        params : 
        info = (userId,)
        '''
        req = 'DELETE FROM gamecollection WHERE gamecollection.idUser = %s'
        try:
            self.connectionDB()
            self.cursor.execute(req, info)
            self.connection.commit()
        except:
            print('Fail to delete games')
        finally: 
            if self.connection.is_connected():
                self.connection.close()

    def delOneGame(self, name):
        '''
        to delete a game
        params : 
        info = (gameName,)
        '''
        req = 'DELETE FROM jeu WHERE jeu.Nom = %s'
        try :
            self.connectionDB()
            self.cursor.execute(req, name)
            self.connection.commit()
        except : 
            print('fail to delete the game')
        finally : 
            if self.connection.is_connected() :
                self.connection.close()

    def updateGame(self, info):
        '''
        to update game informations 
        params :  
        info = (gameName, gamePegi, gameIdGenre, gameIdConsole, gameId)
        '''
        req = 'UPDATE jeu SET jeu.Nom = %s, jeu.pegi = %s, jeu.idGenre = %s, jeu.idConsole = %s WHERE jeu.idJeu = %s'
        try :
            self.connectionDB()
            self.cursor.execute(req, info)
            self.connection.commit()
        except :
            print('Fail to update console') 
        finally:
            if self.connection.is_connected():
                self.connection.close()