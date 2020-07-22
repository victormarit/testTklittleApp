import tkinter
from tkinter import messagebox
from tk.homepageAdminChoices.seeConsole import SeeConsole
from classes.db import DB


class AddConsole:
    def __init__(self, frame):
        global mainFrame
        mainFrame = frame
        self.frameApp = tkinter.Frame(frame)
        self.frameApp.pack()
        #
        self.labelWelcome = tkinter.Label(self.frameApp, text = 'Ajouter une console')
        self.labelWelcome.grid(row = 0, column = 0, columnspan = 2)
        #
        self.labelVoid1 = tkinter.Label(self.frameApp, text = '')
        self.labelVoid1.grid(row = 1, column = 0)
        #
        self.name = tkinter.Label(self.frameApp, text = 'Nom Console : ')
        self.name.grid(row = 2, column = 0)
        self.nameEntry = tkinter.Entry(self.frameApp)
        self.nameEntry.grid(row = 2, column = 1)
        #
        self.constructeur = tkinter.Label(self.frameApp, text = 'Nom Constructeur : ')
        self.constructeur.grid(row = 3, column = 0)
        self.constructeurEntry = tkinter.Entry(self.frameApp)
        self.constructeurEntry.grid(row = 3, column = 1)
        #
        self.annee = tkinter.Label(self.frameApp, text = 'Année : ')
        self.annee.grid(row = 4, column = 0)
        self.anneeEntry = tkinter.Entry(self.frameApp)
        self.anneeEntry.grid(row = 4, column = 1)
        #logo
        self.logo = tkinter.Label(self.frameApp, text = 'Lien Vers Logo : ')
        self.logo.grid(row = 5, column = 0 )
        self.logoEntry = tkinter.Entry(self.frameApp)
        self.logoEntry.grid(row = 5, column = 1 )
        #void
        self.labelVoid2 = tkinter.Label(self.frameApp, text = '')
        self.labelVoid2.grid(row = 6, column = 0)
        #valider
        self.boutonValider = tkinter.Button(self.frameApp, text = 'Valider', width = 10, command = self.valider)
        self.boutonValider.grid(row = 7, column = 0, columnspan = 2, pady= 5)
        #Annuler
        self.boutonAnnuler = tkinter.Button(self.frameApp, text = 'Annuler', width = 10, command = self.cancel)
        self.boutonAnnuler.grid(row = 8, column = 0, columnspan = 2)

    def cancel(self):
        self.frameApp.destroy()
        SeeConsole(mainFrame)
    
    def valider(self):
        if self.nameEntry.get() != '' and self.constructeurEntry.get() != '' and self.anneeEntry.get() != '' : 
            test = messagebox.askokcancel('Valider', 'Etes-vous sur de vouloir ajouter cette console ?')
            if test : 
                info = (self.nameEntry.get(), self.constructeurEntry.get(), self.logoEntry.get(), self.anneeEntry.get())
                bd = DB() 
                bd.addNewConsole(info)
                self.frameApp.destroy()
                SeeConsole(mainFrame)

        else:
            alert = messagebox.showinfo('Erreur', 'Veuillez remplir tous les champs')
            alert.pack()
