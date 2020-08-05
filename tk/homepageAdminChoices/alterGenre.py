import tkinter
from tkinter import messagebox
from tkinter import ttk
from classes.testNewDBConnection.dbGenre import DbGenre
from tk.homepageAdminChoices.seeGenre import SeeGenre

class AlterGenre:
    def __init__(self, frame):
        global mainFrame
        mainFrame = frame
        self.frameApp = tkinter.Frame(frame)
        self.frameApp.pack()
        self.labelWelcome = tkinter.Label(self.frameApp, text = 'Modifier une console')
        self.labelWelcome.pack()
        self.voidLab = tkinter.Label(self.frameApp, text= '')
        self.voidLab.pack()

        self.id = 0
        self.values = []
        self.getAllGenres()
        self.box = ttk.Combobox(self.frameApp, values = self.values, state= 'readonly')
        self.box.pack()
        self.void2 = tkinter.Label(self.frameApp, text = '')
        self.void2.pack()

        self.frameBis = tkinter.Frame(self.frameApp)
        self.frameBis.pack()
        
        self.name = tkinter.Label(self.frameBis, text = 'Nom Genre : ')
        self.name.grid(row = 1, column = 0)
        self.nameEntry = tkinter.Entry(self.frameBis)
        self.nameEntry.grid(row = 1, column = 1)

        self.boutonValider = tkinter.Button(self.frameApp, text = 'Valider', width= 10, command = self.valider)
        self.boutonValider.pack(pady = 5)
        self.boutonAnnuler = tkinter.Button(self.frameApp, text = 'Annuler', width = 10, command = self.annuler)
        self.boutonAnnuler.pack()

        self.box.bind("<<ComboboxSelected>>", self.auto_completion)

    def getAllGenres(self):
        db = DbGenre()
        data = db.findAllGenres()
        for console in data : 
            self.values.append(console[1])

    def delEntry(self):
        self.nameEntry.delete(first=0,last=1000)

    def auto_completion(self, useless):
        self.delEntry()
        info = (self.box.get(),)
        db = DbGenre()
        data = db.findOneGenre(info)
        self.nameEntry.insert(1, data[1])
        self.id = data[0]
    
    def valider(self):
        pass
        if self.nameEntry.get() != '' and self.box.get() != '' : 
            info = (self.nameEntry.get(),  self.id)
            test = messagebox.askokcancel('Valider', 'Etes vous sur de vouloir modifier ce genre')
            if test : 
                db = DbGenre()
                db.updateGenre(info) 
                self.frameApp.destroy()
                SeeGenre(mainFrame)
        else : 
            messagebox.showinfo("Erreur", 'Veuillez remplir tous les champs')

    def annuler(self):
        self.frameApp.destroy()
        SeeGenre(mainFrame)
