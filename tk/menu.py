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
        #first choice
        self.first_menu=tkinter.Menu(self.mainMenu, tearoff=0)
        self.first_menu.add_command(label="Mon Compte")
        self.first_menu.add_command(label="Déconnexion", command = self.logOut)
        self.first_menu.add_separator()
        self.first_menu.add_command(label="Quitter",command=f1.window.quit)
        #second choice 
        self.second_menu=tkinter.Menu(self.mainMenu, tearoff = 0)
        self.second_menu.add_command(label="commande1")
        self.second_menu.add_command(label="commande2")
        self.second_menu.add_command(label="commande3")
        self.mainMenu.add_cascade(label="Premier",menu=self.first_menu)
        self.mainMenu.add_cascade(label="Second",menu=self.second_menu)
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