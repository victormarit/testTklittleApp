import tkinter
from tkinter import messagebox
from tkinter import ttk

from tk.homepageUserChoices.seeConsole import SeeConsole

import classes.db 

class AddConsole:
    def __init__(self, frame, user):
        global mainFrame
        global utilisateur 
        utilisateur = user
        mainFrame = frame
        self.frameApp = tkinter.Frame(frame)
        self.frameApp.pack()
        #
        self.labelWelcome = tkinter.Label(self.frameApp, text = 'Ajouter une Console')
        self.labelWelcome.pack()
        #
        self.labelVoid1 = tkinter.Label(self.frameApp, text = '')
        self.labelVoid1.pack()
        #
        self.values = []
        self.getAllConsole()
        self.box = ttk.Combobox(self.frameApp, values = self.values, state= 'readonly')
        self.box.pack()
        #
        self.boutonValider = tkinter.Button(self.frameApp, text = 'Valider', width= 10, command = self.valider)
        self.boutonValider.pack(pady = 5)
        self.boutonAnnuler = tkinter.Button(self.frameApp, text = 'Annuler', width = 10, command = self.annuler)
        self.boutonAnnuler.pack()


    def getAllConsole(self):
        db = classes.db.DB()
        data = db.findConsoles()
        for Console in data : 
            self.values.append(Console[1])

    def valider(self):
        #Create an function to find console with id
        db = classes.db.DB()
        data = db.findConsole((self.box.get(),))
        print(data)
        info = (utilisateur.id, data[0] )
        test = messagebox.askyesno('Valider', 'Possédez vous cette console ? ')
        if test :  
            db.insertConsoleUser(info)
            self.annuler()


    def annuler(self):
        self.frameApp.destroy()
        SeeConsole(mainFrame, utilisateur)
        db = classes.db.DB()
        