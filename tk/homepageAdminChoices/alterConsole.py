import tkinter
from tkinter import messagebox
from tkinter import ttk
from classes.db import DB
from tk.homepageAdminChoices.seeConsole import SeeConsole

class AlterConsole:
    def __init__(self, frame):
        global mainFrame
        mainFrame = frame
        self.frameApp = tkinter.Frame(frame)
        self.frameApp.pack()
        self.labelWelcome = tkinter.Label(self.frameApp, text = 'Modifier une console')
        self.labelWelcome.pack()
        self.voidLab = tkinter.Label(self.frameApp, text= '')
        self.voidLab.pack()

        self.values = []
        self.getAllConsoles()
        self.box = ttk.Combobox(self.frameApp, values = self.values, state= 'readonly')
        self.box.pack()

        self.frameBis = tkinter.Frame(self.frameApp)
        self.frameBis.pack()
        
        self.name = tkinter.Label(self.frameBis, text = 'Nom Console : ')
        self.name.grid(row = 1, column = 0)
        self.nameEntry = tkinter.Entry(self.frameBis)
        self.nameEntry.grid(row = 1, column = 1)
        #
        self.constructeur = tkinter.Label(self.frameBis, text = 'Nom Constructeur : ')
        self.constructeur.grid(row = 2, column = 0)
        self.constructeurEntry = tkinter.Entry(self.frameBis)
        self.constructeurEntry.grid(row = 2, column = 1)
        #
        self.annee = tkinter.Label(self.frameBis, text = 'Année : ')
        self.annee.grid(row = 3, column = 0)
        self.anneeEntry = tkinter.Entry(self.frameBis)
        self.anneeEntry.grid(row = 3, column = 1)
        #logo
        self.logo = tkinter.Label(self.frameBis, text = 'Lien Vers Logo : ')
        self.logo.grid(row = 4, column = 0 )
        self.logoEntry = tkinter.Entry(self.frameBis)
        self.logoEntry.grid(row = 4, column = 1 )

        self.boutonValider = tkinter.Button(self.frameApp, text = 'Valider', width= 10, command = self.valider)
        self.boutonValider.pack(pady = 5)
        self.boutonAnnuler = tkinter.Button(self.frameApp, text = 'Annuler', width = 10, command = self.annuler)
        self.boutonAnnuler.pack()

        self.box.bind("<<ComboboxSelected>>", self.auto_completion)

    def getAllConsoles(self):
        db = DB()
        data = db.findConsoles()
        for console in data : 
            self.values.append(console[1])

    def auto_completion(self, useless):
        #add delete 
        self.nameEntry.delete(first=0,last=1000)
        self.constructeurEntry.delete(first=0,last=1000)
        self.logoEntry.delete(first=0,last=1000)
        self.anneeEntry.delete(first=0,last=1000)
        info = (self.box.get(),)
        print(info)
        db = DB()
        data = db.findConsole(info)
        self.nameEntry.insert(1, data[1])
        self.constructeurEntry.insert(2, data[2])
        self.logoEntry.insert(4, data[3])
        self.anneeEntry.insert(3, data[4])
    
    def valider(self):
        if self.nameEntry.get() != '' and self.constructeurEntry.get() != '' and self.anneeEntry.get() != '' and self.box.get() !='' : 
            test = messagebox.askokcancel('Valider', 'Etes vous sur de vouloir modifier cette console')
            if test : 
                #db = DB()
                #db.alterConsole() #create fonction
                self.frameApp.destroy()
                SeeConsole(mainFrame)
        else : 
            messagebox.showinfo("Erreur", 'Veuillez remplir tous les champs')

    def annuler(self):
        self.frameApp.destroy()
        SeeConsole(mainFrame)
