import tkinter
from tkinter import ttk
from tkinter import messagebox

from classes.testNewDBConnection.dbConsole import DbConsole
from tk.homepageAdminChoices.seeConsole import SeeConsole


class DelConsole:
    def __init__(self, frame):
        global mainFrame
        mainFrame = frame
        self.frameApp = tkinter.Frame(frame)
        self.frameApp.pack()
        #
        self.labelWelcome = tkinter.Label(self.frameApp, text = 'Supprimer une Console')
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
        db = DbConsole()
        data = db.findAllConsoles()
        for Console in data : 
            self.values.append(Console[1])
    
    def annuler(self):
        self.frameApp.destroy()
        SeeConsole(mainFrame)

    def valider(self):
        info = (self.box.get(),)
        test = messagebox.askokcancel('Valider', 'Etes-vous sur de vouloir supprimer ce contenu')
        if test : 
            db = DbConsole()
            db.deleteConsole(info)
            self.frameApp.destroy()
            SeeConsole(mainFrame)



