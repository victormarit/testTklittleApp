import tkinter 
from tkinter import messagebox

from fonctions.fonctionsTk import hashPassword
from classes.db import DB

class DelAccount:
    def __init__(self, utilisateur, frame, father):
        global frame1
        global user 
        global parent
        parent = father
        user = utilisateur
        frame1 = frame

        self.frameApp = tkinter.Frame(frame)
        self.frameApp.pack()

        self.label = tkinter.Label(self.frameApp, text = 'Suppression du compte')
        self.label.grid(row = 0, column = 0, columnspan = 2)

        self.void = tkinter.Label(self.frameApp, text = '')
        self.void.grid(row = 1, column = 0)

        self.pw = tkinter.Label(self.frameApp, text = 'Mot de passe : ')
        self.pw.grid(row = 2, column = 0)

        self.pwEntry = tkinter.Entry(self.frameApp, show = '*')
        self.pwEntry.grid(row = 2, column = 1)

        self.buttonValider = tkinter.Button(self.frameApp, text = 'Supprimer', width = 10, command = self.supprimer)
        self.buttonValider.grid(row = 3, column = 0, columnspan =2, pady = 5)
        self.buttonAnnuler = tkinter.Button(self.frameApp, text = 'Annuler', width = 10, command = self.annuler)
        self.buttonAnnuler.grid(row = 4, column = 0, columnspan =2)

    def annuler(self):
        widget = frame1.winfo_children()
        for i in widget : 
            i.destroy()

    def supprimer(self):
        if self.pwEntry.get() != '':
            pw = hashPassword(self.pwEntry.get())
            if pw == user.password :
                if user.admin:
                    messagebox.showinfo('Attention', 'Un administrateur ne peut supprimer son compte')
                    self.annuler()
                else: 
                    test = messagebox.askokcancel("Valider", 'Etes vous sûr de vouloir supprimer votre compte ?')
                    if test : 
                        info = (user.nom, user.prenom, user.email, user.password)
                        bdd = DB()
                        bdd.deleteUser(info)
                        messagebox.showinfo('Information', 'Votre compte a été supprimé, merci d\'avoir utilisé notre plateforme')
                        parent.logOut()
            else: 
                messagebox.showinfo("Erreur", 'Erreur dans la saisie du mot de passe')
        else : 
            messagebox.showinfo('Erreur', 'Veuillez renseigner votre mot de passe ')