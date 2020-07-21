import tkinter
from tkinter import ttk
import classes.db
from tkinter import messagebox
from tk.homepageAdminChoices.seeGenre import SeeGenre

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
        self.spinbox = ttk.Spinbox(self.frameApp, values = self.values)
        self.spinbox.pack()
        #
        self.boutonValider = tkinter.Button(self.frameApp, text = 'Valider', width= 10, command = self.valider)
        self.boutonValider.pack(pady = 5)
        self.boutonAnnuler = tkinter.Button(self.frameApp, text = 'Annuler', width = 10, command = self.annuler)
        self.boutonAnnuler.pack()


    def getAllGenre(self):
        db = classes.db.DB()
        data = db.findGenres()
        for genre in data : 
            self.values.append(genre[1])
    
    def annuler(self):
        self.frameApp.destroy()
        SeeGenre(mainFrame)

    def valider(self):
        info = (self.spinbox.get(),)
        print(info)
        test = messagebox.askokcancel('Valider', 'Etes-vous sur de vouloir supprimer ce contenu')
        if test : 
            db = classes.db.DB()
            db.deleteOldGenre(info)
            self.frameApp.destroy()
            SeeGenre(mainFrame)



