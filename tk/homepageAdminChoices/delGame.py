import tkinter
from tkinter import messagebox
from tkinter import ttk

from classes.testNewDBConnection.dbGame import DbGame
from tk.homepageAdminChoices.addGame import AddGame

class DelGame:
    def __init__(self, frame):
        self.frame = frame
        self.frameApp = tkinter.Frame(self.frame)
        self.frameApp.pack(side = 'left', fill='both', expand=1)
        #
        self.secondFrame = tkinter.Frame(self.frameApp)
        self.secondFrame.pack(side = 'top', fill='both', expand= 1 )
        #
        self.label = tkinter.Label(self.secondFrame, text = 'Supprimer un jeu :')
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
        self.nbEntry = 0
        self.data = 0
    

    def findGame(self):
        test = DbGame()
        self.data = test.getGameSearch(self.entryGame.get())
        if len(self.data) == 0 :
            test = messagebox.showerror('Aucun résultat', 'Aucun jeu correspondant à votre demande')
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
        addButton = tkinter.Button(self.thridFrame, width = 15, text = 'Supprimer', command = self.delTheGame)
        addButton.grid(row = 5, column = 0, columnspan = 2, pady = 10)
        returnButton = tkinter.Button(self.thridFrame, width = 15, text = 'Annuler', command = self.returnMenu)
        returnButton.grid(row = 6, column = 0, columnspan = 2)

    def delTheGame(self):
        try :
            name = self.listbox.get(self.listbox.curselection())
            test = messagebox.askokcancel("Supprimer", "Êtes-vous sûr de vouloir supprimer ce jeu ?")
            if test:
                database = DbGame()
                database.delOneGame((name,))
                self.returnMenu()
        except: 
            messagebox.showerror("Erreur", "Veuillez sélectionner un jeu")
    
    def returnMenu(self):
        self.frameApp.destroy()
        AddGame(self.frame)

