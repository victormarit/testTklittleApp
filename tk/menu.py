import tkinter
import tk.connection
import tk.homepageAdmin
import tk.homepageUser

class MenuTK:
    def __init__(self, f1, utilisateur):
        global fenetre
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
        self.second_menu.add_command(label="Informations")
        self.second_menu.add_command(label="Changer mot de passe")
        self.second_menu.add_command(label="Supprimer mon compte")    
        #third menu 
        self.third_menu = tkinter.Menu(self.mainMenu, tearoff = 0)
        self.third_menu.add_command(label = "Pannel administratif")
        self.third_menu.add_command(label = "Voir ma collection")
        #
        self.mainMenu.add_cascade(label="Application",menu=self.first_menu)
        self.mainMenu.add_cascade(label="Mon Compte",menu=self.second_menu)
        self.addThirdMenu(utilisateur)
        f1.window.config(menu = self.mainMenu)
        self.userOrAdmin(utilisateur)
    
    def userOrAdmin(self, user):
        if user.admin : 
            self.frame = tk.homepageAdmin.HomepageAdmin(fenetre, user)
        else : 
            self.frame = tk.homepageUser.HomepageUser(fenetre, user)

    def logOut(self):
        self.mainMenu.destroy()
        self.frame.frameHomepage.destroy()
        self.frame.frame1.destroy()
        tk.connection.FrameConnection(fenetre)
    
    def addThirdMenu(self, user):
        if user.admin : 
            self.mainMenu.add_cascade(label = 'admin', menu= self.third_menu)