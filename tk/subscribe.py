import tkinter
from tkinter import messagebox
import tk.connection
import classes.db
import classes.user
import fonctions.fonctionsTk
import tk.menu
import re

class Subscribe :
    def __init__(self, fenetre) :
        global f1
        f1 = fenetre
        self.mainFrame = tkinter.Frame(fenetre.window)
        self.mainFrame.pack()
        self.label = tkinter.Label(self.mainFrame, text = "Inscription")
        self.label.grid(row = 0, column = 0 , columnspan = 2)
        self.voidLabel = tkinter.Label(self.mainFrame, text = "")
        self.voidLabel.grid(row = 1, column = 0)
        self.fn = tkinter.Label(self.mainFrame, text = "Prenom : ")
        self.fn.grid(row = 2, column = 0)
        self.fnEntry = tkinter.Entry(self.mainFrame)
        self.fnEntry.grid(row = 2, column = 1)
        self.ln = tkinter.Label(self.mainFrame, text = "Nom : ")
        self.ln.grid(row = 3, column = 0)
        self.lnEntry = tkinter.Entry(self.mainFrame)
        self.lnEntry.grid(row = 3, column = 1)
        self.email = tkinter.Label(self.mainFrame, text = 'Email : ')
        self.email.grid(row = 4, column = 0)
        self.emailEntry = tkinter.Entry(self.mainFrame)
        self.emailEntry.grid(row = 4, column = 1)
        self.mp = tkinter.Label(self.mainFrame, text = 'Mot de passe : ')
        self.mp.grid(row = 5, column = 0)
        self.mpEntry = tkinter.Entry(self.mainFrame, show ='*')
        self.mpEntry.grid(row = 5, column = 1)
        self.valider = tkinter.Button(self.mainFrame, text = "Valider", width = 10, command = self.valider)
        self.valider.grid(row = 6, column = 0, columnspan = 2)
        self.retour = tkinter.Button(self.mainFrame, text = "Annuler", width = 10, command = self.retour)
        self.retour.grid(row = 7, column = 0, columnspan = 2)

    def valider(self):
        if(self.lnEntry.get() != '' and self.fnEntry.get() != '' and self.emailEntry.get() and self.mpEntry.get()):
            if not re.match(r"[^@]+@[^@]+\.[^@]+", self.emailEntry.get()):
                messagebox.showinfo('Erreur','Adresse email invalide')
            else :
                bdd = classes.db.DB()
                test = bdd.testEmail(self.emailEntry.get())
                if test :
                    password = fonctions.fonctionsTk.hashPassword(self.mpEntry.get())
                    data = (self.lnEntry.get(), self.fnEntry.get(), self.emailEntry.get(), password)
                    connection = (self.emailEntry.get(), password)
                    bdd.subscribe(data)
                    info = bdd.login(connection)
                    utilisateur = classes.user.User(info)
                    self.mainFrame.destroy()
                    tk.menu.MenuTK(f1, utilisateur)
                elif test == False :
                    messagebox.showinfo("Erreur", "Cette adresse email est déjà utilisée") 
                else : 
                    messagebox.showinfo("Erreur", "Echec de la connexion à la base de données rééssayer ultérieurement")
        else : 
            messagebox.showinfo('Erreur', 'Veuillez remplir tous les champs')


    def retour(self): 
        self.mainFrame.destroy()
        tk.connection.FrameConnection(f1)