import tkinter
from tkinter import messagebox
from tkinter import ttk

from classes.testNewDBConnection.dbGame import DbGame 
from classes.testNewDBConnection.dbConsole import DbConsole 
from classes.testNewDBConnection.dbGenre import DbGenre
from tk.homepageAdminChoices.addGame import AddGame

class AlterGame:
    def __init__(self, frame):
        self.frame = frame
        self.frameApp = tkinter.Frame(self.frame)
        self.frameApp.pack(side = 'left', fill='both', expand=1)
        #
        self.secondFrame = tkinter.Frame(self.frameApp)
        self.secondFrame.pack(side = 'top', fill='both', expand= 1 )
        #
        self.label = tkinter.Label(self.secondFrame, text = 'Modifier un jeu :')
        self.label.pack()
        self.void = tkinter.Label(self.secondFrame, text = '')
        self.void.pack()
        #
        self.thridFrame = tkinter.Frame(self.secondFrame)
        self.thridFrame.pack()
        self.entryGame = tkinter.Entry(self.thridFrame)
        self.entryGame.grid(row = 2, column = 0, sticky = 'e')
        self.searchButton = tkinter.Button(self.thridFrame, text = 'Rechercher', command = self.findGame)
        self.searchButton.grid(row = 2, column = 1, padx = 5, sticky ='w')
        #
        self.listbox = 0
        self.data = 0
        self.name = ''
        self.pegi = 0
        self.genre = ''
        self.console = ''
        self.id = 0
        self.listGenres = []
        self.listConsoles = []

    def findGame(self):
        test = DbGame()
        self.data = test.getGameSearch(self.entryGame.get())
        if len(self.data) == 0 :
            test = messagebox.askyesno('Erreur', 'Il n\'y a pas de jeu correspondat dans la base de données')
        elif len(self.data) > 0:
            self.listGame(self.data)
        else:
            messagebox.showerror('Erreur', 'Connexion à la base de données perdue')
    
    def listGame(self, games):
        void = tkinter.Label(self.thridFrame, text = '')
        void.grid(row = 3, column = 0)
        scrollbar = tkinter.Scrollbar(self.thridFrame)
        self.listbox = tkinter.Listbox(self.thridFrame, width = 55, height = 10)
        i = 0 
        for game in games : 
            self.listbox.insert(i, game[1])
            i+=1
        self.listbox.grid(row = 4, column = 0, columnspan = 2)
        scrollbar.grid(row = 4, column = 3, sticky = 'ns')
        scrollbar.config( command = self.listbox.yview )
        addButton = tkinter.Button(self.thridFrame, width = 15, text = 'Modifier', command = self.customGame)
        addButton.grid(row = 5, column = 0, columnspan = 2, pady = 10)
        cancelButton = tkinter.Button(self.thridFrame, width = 15, text = 'Annuler', command = self.cancel)
        cancelButton.grid(row = 6, column = 0, columnspan = 2)

    def cancel(self) :
        self.frameApp.destroy()
        AddGame(self.frame)

    def customGame(self) :
        try : 
            self.name = self.listbox.get(self.listbox.curselection())
            test = messagebox.askokcancel("Modifier", "Êtes-vous sûr de vouloir modifier ce jeu ?")
            if test : 
                self.alterGame2()
        except:
            messagebox.showerror('Erreur', 'Veuillez sélectionner un jeu à modifier')
    
    def alterGame2(self) :
        #destroy previous frame
        self.frameApp.destroy()
        #find the game
        self.getGameInformation()
        self.getGenre()
        self.getConsole()
        #tkinter inferface
        frameApp = tkinter.Frame(self.frame)
        frameApp.pack()
        label = tkinter.Label(frameApp, text = 'Modifier un jeu')
        label.grid(row = 0, column = 0, columnspan = 3)
        voidLabel = tkinter.Label(frameApp, text = '')
        voidLabel.grid(row = 1, column = 0)
        name = tkinter.Label(frameApp, text = 'Nom du jeu :')
        name.grid(row = 2, column = 0, sticky = 'w')
        nameEntry = tkinter.Entry(frameApp, width = 23)
        nameEntry.insert(1, self.name)
        nameEntry.grid(row = 2, column = 1)
        console = tkinter.Label(frameApp, text = 'Console :')
        console.grid(row = 3, column = 0,  sticky = 'w')
        consoleEntry = ttk.Combobox(frameApp, values = self.listConsoles ,state= 'readonly', width = 20)
        if self.console:
            for i in range(len(self.listConsoles)):
                if self.console == self.listConsoles[i] : 
                    consoleEntry.current(i)
        consoleEntry.grid(row = 3, column = 1)
        pegi = tkinter.Label(frameApp, text = 'Pegi :')
        pegi.grid(row = 4, column = 0,  sticky = 'we')
        pegiEntry = tkinter.Entry(frameApp, width = 23)
        pegiEntry.insert(1, self.pegi)
        pegiEntry.grid(row = 4, column = 1)
        genre = tkinter.Label(frameApp, text = 'Genre :')
        genre.grid(row = 5, column = 0,  sticky = 'w')
        genreBox = ttk.Combobox(frameApp, values = self.listGenres ,state = 'readonly', width = 20)
        if self.genre :
            for i in range(len(self.listGenres)):
                if self.genre == self.listGenres[i] : 
                    genreBox.current(i)
        genreBox.grid(row = 5, column = 1)
        buttonAddGame = tkinter.Button(frameApp, text = "Modifier", width = 10)
        buttonAddGame.grid(row=6, column = 0, columnspan = 2, pady = 5)
        buttonReturn = tkinter.Button(frameApp, text = 'Annuler', width = 10, command = self.cancel2)
        buttonReturn.grid(row=7, column = 0, columnspan = 2)

    def getGameInformation(self):
        db = DbGame()
        game = db.getGameSearch(self.name)
        self.pegi =game[0][2]
        self.id = game[0][0]
        self.genre =  game[0][3]
        self.console =  game[0][4]
    
    def getGenre(self):
        database = DbGenre()
        genres = database.findAllGenres()
        for genre in genres : 
            self.listGenres.append(genre[1])
        if self.genre :
            self.genre = database.findGenreWithId((self.genre,))
        
    def getConsole(self):
        database = DbConsole()
        consoles = database.findAllConsoles()
        for console in consoles : 
            self.listConsoles.append(console[1])
        if self.console :
            self.console = database.findConsoleWithId((self.console,))

    def cancel2(self):
        widget = self.frame.winfo_children()
        for i in widget :
            i.destroy()
        AlterGame(self.frame)