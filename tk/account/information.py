import tkinter 
from tkinter import messagebox

from fonctions.fonctionsTk import hashPassword
from classes.db import DB

class UserInformation : 
    def __init__(self, utilisateur, frame):
        global frame1
        global user 
        user = utilisateur
        frame1 = frame
        self.frameApp = tkinter.Frame(frame)
        self.frameApp.pack()
        self.labelWelcome = tkinter.Label(self.frameApp, text = 'Mes informations')
        self.labelWelcome.grid(row = 0, column = 0, columnspan = 2)

        self.void = tkinter.Label(self.frameApp, text = '')
        self.void.grid(row=1, column=0)

        self.prenom = tkinter.Label(self.frameApp, text = "Prénom : ")
        self.prenom.grid(row = 2, column = 0)
        self.prenomEntry = tkinter.Entry(self.frameApp)
        self.prenomEntry.insert(1, utilisateur.prenom)
        self.prenomEntry.grid(row = 2, column = 1)

        self.nom = tkinter.Label(self.frameApp, text = 'Nom : ')
        self.nom.grid(row = 3, column = 0)
        self.nomEntry = tkinter.Entry(self.frameApp)
        self.nomEntry.insert(1, utilisateur.nom)
        self.nomEntry.grid(row = 3, column = 1)

        self.email = tkinter.Label(self.frameApp, text = 'Email : ')
        self.email.grid(row = 4, column = 0)
        self.emailEntry = tkinter.Entry(self.frameApp)
        self.emailEntry.insert(1, utilisateur.email)
        self.emailEntry.grid(row = 4, column = 1)

        self.pw = tkinter.Label(self.frameApp, text = 'Mot de passe : ')
        self.pw.grid(row = 5 , column = 0)
        self.pwEntry = tkinter.Entry(self.frameApp, show ='*')
        self.pwEntry.grid(row = 5, column = 1)

        self.boutonModif = tkinter.Button(self.frameApp, text = 'Modifier', width = 10, command = self.modifier)
        self.boutonModif.grid(row = 6, column = 0, columnspan = 2, pady = 5)
        self.boutonCancel = tkinter.Button(self.frameApp, text = 'Annuler', width = 10, command = self.annuler)
        self.boutonCancel.grid(row = 7, column = 0, columnspan = 2)
    
    def annuler(self):
        widget = frame1.winfo_children()
        for i in widget : 
            i.destroy()
        

    def modifier(self):
        if self.prenomEntry.get() != '' and self.nomEntry.get() != '' and self.emailEntry.get() != '' and self.pwEntry.get() != '':   
            test = self.controlPW() 
            if test :
                test2 = messagebox.askokcancel('Modifier', 'Etes vous sur de vouloir modifier vos informations ?')
                if test2:
                    self.updateUser()
                    self.updateUserInDB()
                    messagebox.showinfo('Modification', 'Vos données ont été mises à jour')
                    self.annuler()
            else : 
                messagebox.showinfo("Erreur", 'Le mot de passe entré est faux')
        else :
            messagebox.showinfo("Erreur", 'Veuillez remplir tous les champs')

    def updateUser(self):
        info = (self.prenomEntry.get(), self.nomEntry.get(), self.emailEntry.get())
        user.updateUserInformations(info)

    def updateUserInDB(self):
        info = (user.nom, user.prenom, user.email, user.id)
        bdd = DB()
        bdd.updateUser(info)

    def controlPW(self):
        pw = hashPassword(self.pwEntry.get())
        if pw == user.password:
            return True
        else : 
            return False