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
        req = f'SELECT  jeu.Nom FROM jeu WHERE jeu.Nom LIKE "% {idUser} %"'
        try:
            self.connectionDB()
            self.cursor.execute(req)
            data = self.cursor.fetchall()
        except :
            print('Fail to find game')
        finally:
            if self.connection.is_connected():
                self.connection.close()
                if data is None :
                    return []
                else: 
                    return data
            else:
                return 
        