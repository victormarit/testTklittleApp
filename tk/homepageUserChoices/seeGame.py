import tkinter
from tkinter import messagebox
from classes.testNewDBConnection.dbGame import DbGame

class SeeGame:
    def __init__(self, frame, user):
        self.user = user
        self.frame = frame
        self.frameApp = tkinter.Frame(self.frame)
        self.frameApp.pack()
        #
        self.listNameGame = []
        self.listGameQuantity = []
        self.getGamecollectionInfo()
        self.page()
    
    def getGamecollectionInfo(self):
        db = DbGame()
        games = db.getUserGames((self.user.id,))
        self.getGamesNames(games)

    def getGamesNames(self, games):
        db = DbGame()
        for game in games :
            name = db.getGameName((game[1],))
            self.listNameGame.append(name)
            self.listGameQuantity.append(game[2])

    def page(self):
        if len(self.listNameGame):
            welcomeLabel = tkinter.Label(self.frameApp, text = 'Vos jeux')
            welcomeLabel.grid(row = 0 , column = 0, columnspan = 10)
            for i in range(len(self.listNameGame)):
                label = tkinter.Label(self.frameApp, text = self.listNameGame[i][0])
                label.grid()
        else : 
            label = tkinter.Label(self.frameApp, text = 'Vous n\'avez pas de jeu')
            label.grid()