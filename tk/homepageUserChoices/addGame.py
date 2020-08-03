import tkinter
from tkinter import messagebox
from tkinter import ttk

from classes.testNewDBConnection.dbGame import DbGame 

from tk.homepageUserChoices.addGameInDb import AddGameInDB

class AddGame:
    def __init__(self, frame, user):
        self.utilisateur = user
        self.frame = frame
        self.frameApp = tkinter.Frame(self.frame)
        self.frameApp.pack(side = 'left', fill='both', expand=1)
        #
        self.secondFrame = tkinter.Frame(self.frameApp)
        self.secondFrame.pack(side = 'top', fill='both', expand= 1 )
        #
        self.label = tkinter.Label(self.secondFrame, text = 'Ajouter un jeu :')
        self.label.pack()
        self.void = tkinter.Label(self.secondFrame, text = '')
        self.void.pack()
        #
        self.thridFrame = tkinter.Frame(self.secondFrame)
        self.thridFrame.pack()
        self.entryGame = tkinter.Entry(self.thridFrame)
        self.entryGame.grid(row = 2, column = 0)
        self.searchButton = tkinter.Button(self.thridFrame, text = 'Rechercher', command = self.findGame)
        self.searchButton.grid(row = 2, column = 1, padx = 5)
    

    def findGame(self):
        test = DbGame()
        data = test.getUserGames(self.utilisateur.id)
        if len(data) == 0 :
            test = messagebox.askyesno('Ajouter Jeu', 'Pas de jeux correspondant, voulez vous l\'ajouter ?')
            if test == True : 
                self.newGame()
        elif len(data) > 0:
            messagebox.showinfo('Erreur', 'La fonction n\'a pas encore été implémenté')
        else:
            messagebox.showerror('Erreur', 'Connexion à la base de données perdue')
    
    def newGame(self):
        test = self.frame.winfo_children()
        for i in test :
            i.destroy()
        AddGameInDB(self.frame, self.utilisateur)
