import tkinter
from tkinter import ttk
from tkinter import messagebox
from tk.homepageAdminChoices.seeGenre import SeeGenre
from classes.testNewDBConnection.dbGenre import DbGenre

class DelGenre:
    def __init__(self, frame):
        global mainFrame
        mainFrame = frame
        self.frameApp = tkinter.Frame(frame)
        self.frameApp.pack()
        #
        self.labelWelcome = tkinter.Label(self.frameApp, text = 'Supprimer un Genre de Jeu')
        self.labelWelcome.pack()
        #
        self.labelVoid1 = tkinter.Label(self.frameApp, text = '')
        self.labelVoid1.pack()
        #
        self.values = []
        self.getAllGenre()
        self.box = ttk.Combobox(self.frameApp, values = self.values, state= 'readonly')
        self.box.pack()
        #
        self.boutonValider = tkinter.Button(self.frameApp, text = 'Valider', width= 10, command = self.valider)
        self.boutonValider.pack(pady = 5)
        self.boutonAnnuler = tkinter.Button(self.frameApp, text = 'Annuler', width = 10, command = self.annuler)
        self.boutonAnnuler.pack()


    def getAllGenre(self):
        db = DbGenre()
        data = db.findAllGenres()
        for genre in data : 
            self.values.append(genre[1])
    
    def annuler(self):
        self.frameApp.destroy()
        SeeGenre(mainFrame)

    def valider(self):
        info = (self.box.get(),)
        test = messagebox.askokcancel('Valider', 'Etes-vous sur de vouloir supprimer ce contenu')
        if test : 
            db = DbGenre()
            db.deleteOldGenre(info)
            self.frameApp.destroy()
            SeeGenre(mainFrame)



