import tkinter
from tkinter import messagebox
from tkinter import ttk
from tk.homepageUserChoices.seeConsole import SeeConsole

from classes.testNewDBConnection.dbConsoleCollection import DbConsoleCollection
from classes.testNewDBConnection.dbConsole import DbConsole

class AddConsole:
    def __init__(self, frame, user):
        global mainFrame
        global utilisateur 
        utilisateur = user
        mainFrame = frame
        self.values = []
        #Frame
        self.frameApp = tkinter.Frame(frame)
        self.frameApp.pack()
        #Label
        self.labelWelcome = tkinter.Label(self.frameApp, text = 'Ajouter une Console')
        self.labelWelcome.grid(row =0, column = 0, columnspan = 2)
        self.labelVoid1 = tkinter.Label(self.frameApp, text = '')
        self.labelVoid1.grid(row =1, column = 0)
        #Combobox with all consoles
        self.getAllConsole()
        self.box = ttk.Combobox(self.frameApp, values = self.values, state= 'readonly')
        self.box.grid(row = 2, column = 0, columnspan = 2)
        #void lab 2
        self.labelVoid2 = tkinter.Label(self.frameApp, text = '')
        self.labelVoid2.grid(row =3, column = 0)
        #quantity console
        self.quant = tkinter.Label(self.frameApp, text = 'Quantité enregistrée : ')
        self.quant.grid(row = 4, column = 0)
        self.quantLab = tkinter.Label(self.frameApp, text = '0')
        self.quantLab.grid(row = 4, column = 1)
        self.newQuant = tkinter.Label (self.frameApp, text = 'Quantité possédée : ')
        self.newQuant.grid(row = 5, column = 0)
        self.newQuantEntry = tkinter.Entry(self.frameApp)
        self.newQuantEntry.grid(row = 5, column = 1)
        #
        self.boutonValider = tkinter.Button(self.frameApp, text = 'Valider', width= 10, command = self.valider)
        self.boutonValider.grid(row = 6, column = 0, columnspan = 2, pady = 5)
        self.boutonAnnuler = tkinter.Button(self.frameApp, text = 'Annuler', width = 10, command = self.annuler)
        self.boutonAnnuler.grid(row = 7, column = 0, columnspan = 2)

        self.box.bind("<<ComboboxSelected>>", self.insertQuantityConsole)


    def getAllConsole(self):
        db = DbConsole()
        data = db.findAllConsoles()
        for Console in data : 
            self.values.append(Console[1])

    def valider(self):
        #Create an function to find console with id
        test1 = self.newQuantEntry.get()
        true = True
        try :
            test1= int(test1)
        except:
            messagebox.showerror('Alert', 'La quantité possédée doit être un nombre entier positif')
            true = False 
        if test1<0 :
            messagebox.showerror('Alert', 'La quantité possédée doit être un nombre entier positif')
        else: 
            if true and self.box.get() != '':
                db = DbConsole()
                database = DbConsoleCollection()
                if int(self.quantLab.cget('text')) == 0 and test1 > 0 :
                    data = db.findOneConsole((self.box.get(), ))
                    info = (utilisateur.id, data[0], test1)
                    test = messagebox.askyesno('Valider', 'Ajouter cette console ? ')
                    if test :  
                        database.insertConsoleUser(info)
                        self.annuler()
                elif int(self.quantLab.cget('text')) != 0 and test1 > 0 :
                    data = db.findOneConsole((self.box.get(), ))
                    info = (test1, data[0], utilisateur.id)
                    test = messagebox.askyesno('Valider', 'Modifier la quantité ? ')
                    if test :
                        database.updateConsoleUser(info)
                        self.annuler()
                else :
                    data = db.findOneConsole((self.box.get(), ))
                    info = (utilisateur.id, data[0])
                    test = messagebox.askyesno('Supprimer', 'Etes vous sur de vouloir supprimer cette console ?')
                    if test :  
                        database.deleteConsoleUser(info)
                        self.annuler()

    def insertQuantityConsole(self, useless):
        info = (utilisateur.id, self.box.get())
        database = DbConsoleCollection()
        data = database.userConsoleCollectionQuantity(info)
        if len(data) > 0:
            self.quantLab.config(text = data[0] )
        else: 
            self.quantLab.config(text = 0 )

    def annuler(self):
        self.frameApp.destroy()
        SeeConsole(mainFrame, utilisateur)
        