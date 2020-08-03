import tkinter 
from tkinter import messagebox
from tkinter import ttk

from classes.testNewDBConnection.dbConsole import DbConsole
from classes.testNewDBConnection.dbGenre import DbGenre

from tk.homepageUserChoices.seeGame import SeeGame


class AddGameInDB:
    def __init__(self, frame, user):
        self.user = user
        #
        self.values = [] 
        self.getConsoles()
        self.valuesGenre = []
        self.getGenres()
        #
        self.frame = frame
        self.secondFrame = tkinter.Frame(self.frame)
        self.secondFrame.pack()
        #
        self.label = tkinter.Label(self.secondFrame, text = 'Ajouter un jeu à la base de données')
        self.label.grid(row = 0, column = 0, columnspan = 10)
        self.voidLabel = tkinter.Label(self.secondFrame, text = '')
        self.voidLabel.grid(row = 1, column = 0)
        self.name = tkinter.Label(self.secondFrame, text = 'Nom du jeu :')
        self.name.grid(row = 2, column = 0, sticky = 'w')
        self.nameEntry = tkinter.Entry(self.secondFrame, width = 23)
        self.nameEntry.grid(row = 2, column = 1)
        self.console = tkinter.Label(self.secondFrame, text = 'Console :')
        self.console.grid(row = 3, column = 0,  sticky = 'w')
        self.consoleEntry = ttk.Combobox(self.secondFrame, values = self.values, state= 'readonly',width = 20)
        self.consoleEntry.grid(row = 3, column = 1)
        self.pegi = tkinter.Label(self.secondFrame, text = 'Pegi :')
        self.pegi.grid(row = 4, column = 0,  sticky = 'we')
        self.pegiEntry = tkinter.Entry(self.secondFrame, width = 23)
        self.pegiEntry.grid(row = 4, column = 1)
        self.genre = tkinter.Label(self.secondFrame, text = 'Genre :')
        self.genre.grid(row = 5, column = 0,  sticky = 'w')
        self.genreBox = ttk.Combobox(self.secondFrame, values = self.valuesGenre, state = 'readonly', width = 20)
        self.genreBox.grid(row = 5, column = 1)
        self.voidLabel2 = tkinter.Label(self.secondFrame, text = '')
        self.voidLabel2.grid(row = 6, column = 0)
        self.buttonAddGame = tkinter.Button(self.secondFrame, text = "Ajouter", width = 10)
        self.buttonAddGame.grid(row=7, column = 0, columnspan = 2, pady = 5)
        self.buttonReturn = tkinter.Button(self.secondFrame, text = 'Annuler', width = 10, command = self.returnMenu)
        self.buttonReturn.grid(row=8, column = 0, columnspan = 2)

    def getConsoles(self):
        database = DbConsole()
        data = database.findAllConsoles()
        for console in data :
            self.values.append(console[1])
    
    def getGenres(self):
        database = DbGenre()
        data = database.findAllGenres()
        for genre in data :
            self.valuesGenre.append(genre[1])

    def returnMenu(self):
        self.secondFrame.destroy()
        SeeGame(self.frame, self.user)

    def addGame(self):
        if self.nameEntry.get() == '' and self.pegiEntry.get() == '' and self.consoleEntry.get() == '' and self.genreBox.get() == '':
            messagebox.showerror('Attention', 'Veuillez remplir tous les champs')
        else:
            #try pegiEntry
            pass
