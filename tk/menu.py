import tkinter
from tkinter import messagebox
import tk.connection
import tk.homepageAdmin
import tk.homepageUser

from tk.account.information import UserInformation
from tk.account.updateUserPassword import UpdateUserPassword
from tk.account.delAccount import DelAccount

class MenuTK:
    def __init__(self, f1, utilisateur):
        global fenetre
        global user
        user = utilisateur
        fenetre = f1
        self.frame = ''
        self.mainMenu=tkinter.Menu(f1.window)
        #first menu
        self.first_menu=tkinter.Menu(self.mainMenu, tearoff=0)
        self.first_menu.add_command(label="Déconnexion", command = self.logOut)
        self.first_menu.add_separator()
        self.first_menu.add_command(label="Quitter",command=f1.window.quit)
        #second menu 
        self.second_menu=tkinter.Menu(self.mainMenu, tearoff = 0)
        self.second_menu.add_command(label="Informations", command = self.userInformation)
        self.second_menu.add_command(label="Changer mot de passe", command = self.userPassword)
        self.second_menu.add_command(label="Supprimer mon compte", command = self.userCloseAccount)    
        #third menu 
        self.third_menu = tkinter.Menu(self.mainMenu, tearoff = 0)
        self.third_menu.add_command(label = "Pannel administratif", command = self.goPannelAdmin)
        self.third_menu.add_command(label = "Voir ma collection", command = self.goMyCollection)
        #
        self.mainMenu.add_cascade(label="Application",menu=self.first_menu)
        self.mainMenu.add_cascade(label="Mon Compte",menu=self.second_menu)
        self.addThirdMenu()
        f1.window.config(menu = self.mainMenu)
        self.userOrAdmin()
    
    def userOrAdmin(self):
        if user.admin : 
            self.frame = tk.homepageAdmin.HomepageAdmin(fenetre, user)
        else : 
            self.frame = tk.homepageUser.HomepageUser(fenetre, user)

    def logOut(self):
        self.mainMenu.destroy()
        self.frame.frameHomepage.destroy()
        self.frame.frame1.destroy()
        tk.connection.FrameConnection(fenetre)
    
    def addThirdMenu(self):
        if user.admin : 
            self.mainMenu.add_cascade(label = 'Admin', menu= self.third_menu)

    def goPannelAdmin(self):
        test = fenetre.window.winfo_children()
        for i in test :
            if i != self.mainMenu:
                i.destroy()
        self.frame = tk.homepageAdmin.HomepageAdmin(fenetre, user)
    
    def goMyCollection(self):
        test = fenetre.window.winfo_children()
        for i in test :
            if i != self.mainMenu:
                i.destroy()
        self.frame = tk.homepageUser.HomepageUser(fenetre, user)

    def userInformation(self):
        widget = self.frame.frame1.winfo_children()
        for i in widget :
            i.destroy()
        UserInformation(user, self.frame.frame1)

    def userPassword(self):
        widget = self.frame.frame1.winfo_children()
        for i in widget :
            i.destroy()
        UpdateUserPassword(user, self.frame.frame1)

    def userCloseAccount(self):
        widget = self.frame.frame1.winfo_children()
        for i in widget :
            i.destroy()
        DelAccount(user, self.frame.frame1, self)
        