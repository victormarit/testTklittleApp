import tkinter
from tkinter import messagebox
from fonctions.fonctionsTk import hashPassword
import tk.subscribe
import tk.menu
import classes.db
import classes.user

class FrameConnection :
    def __init__(self, fenetre):
        global f1 
        f1 = fenetre
        self.frameConnection = tkinter.Frame(fenetre.window)
        self.frameConnection.pack()
        self.label = tkinter.Label(self.frameConnection, text = "Bienvenue sur l'appli")
        self.label.grid(row = 0 , column = 0, columnspan = 2, pady = 15)
        self.id = tkinter.Label(self.frameConnection, text = "Email :")
        self.id.grid(row = 1 , column = 0)
        self.idEntry = tkinter.Entry(self.frameConnection)
        self.idEntry.grid(row = 1 , column = 1)
        self.mp = tkinter.Label(self.frameConnection, text = "Mot de passe :")
        self.mp.grid(row = 2 , column = 0)
        self.mpEntry = tkinter.Entry(self.frameConnection, show='*')
        self.mpEntry.grid(row = 2 , column = 1)
        self.valide = tkinter.Button(self.frameConnection, text = "Valider", width = 10, command = self.connexion)
        self.valide.grid(row = 3, column = 0, columnspan = 2, pady = 2)
        self.sub = tkinter.Button(self.frameConnection, text = "S'inscrire", width = 10, command = self.inscription)
        self.sub.grid(row = 4, column = 0, columnspan = 2)

    def inscription(self):
        self.frameConnection.destroy()
        f1.interface = tk.subscribe.Subscribe(f1)

    def connexion(self):
        if(self.idEntry.get() != '' and self.mpEntry.get() != ''):
            password = hashPassword(self.mpEntry.get())
            logs = (self.idEntry.get(), password)
            bdd = classes.db.DB()
            info = bdd.login(logs)
            if info is None : 
                messagebox.showinfo("Erreur", "Echec de la connexion à la base de données")
            elif info == [] :
                messagebox.showinfo("Erreur", "Email ou mot de passe incorrect")
            else :
                messagebox.showinfo("Connexion",'Connexion Réussie')
                utilisateur = classes.user.User(info)
                self.frameConnection.destroy()
                tk.menu.MenuTK(f1, utilisateur)
        else : 
            messagebox.showinfo('Erreur', 'Veuillez remplir tous les champs')