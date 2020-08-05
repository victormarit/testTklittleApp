from tkinter import ttk
import tkinter
from tkinter import PhotoImage

from tk.homepageUserChoices.seeConsole import SeeConsole
from tk.homepageUserChoices.addConsole import AddConsole
from tk.homepageUserChoices.seeGame import SeeGame
from tk.homepageUserChoices.addGame import AddGame

class HomepageUser:
    def __init__(self, fenetre, user):
        global f1
        global utilisateur
        utilisateur = user
        f1 = fenetre
        #frameHomepage
        self.frameHomepage = tkinter.Frame(fenetre.window, bg = 'white')
        self.frameHomepage.pack(side = 'left', fill ='y')
        self.labelWelcome = tkinter.Label(self.frameHomepage, text = 'Votre collection', bg = 'white')
        self.labelWelcome.pack(padx = 20)
        #logoConsole
        self.logo = PhotoImage(file = 'img/logo/logoManette.gif').subsample(10, 10)

        #Widget treeview
        self.tree = ttk.Treeview(self.frameHomepage)
        self.tree.pack(expand = 1 , fill= 'both')

        #treeview_console
        self.console = self.tree.insert('', 0, text='Consoles')
        self.tree.insert(self.console, 0, 'item1',text='Voir mes consoles', image = self.logo)
        self.tree.insert(self.console, 1, text='Gérer mes consoles', image = self.logo)

        #treeview_jeu
        self.jeu = self.tree.insert('', 1, text='Jeux')
        self.tree.insert(self.jeu, 0, text='Voir mes jeux')
        self.tree.insert(self.jeu, 1, text='Ajouter un jeu')
        self.tree.insert(self.jeu, 2, text='Supprimer un jeu')
        #treeview_wishList
        self.wishList = self.tree.insert('', 2, text = 'Liste de souhaits')
        self.tree.insert(self.wishList, 0, text = 'Jeux voulus')
        self.tree.insert(self.wishList, 1, text = 'Consoles voulues')


        #find tree
        self.tree.bind("<Double-1>", self.onDoubleClick)

        #frameCanva

        self.frame1 = tkinter.Frame(fenetre.window)
        self.frame1.pack(side = 'left', expand = 1, fill='both')

    def onDoubleClick(self, event):
        item = self.tree.identify('item',event.x,event.y)
        if self.tree.item(item, 'text') == 'Voir mes consoles':
            self.testFrame1_destroyChildren()
            SeeConsole(self.frame1, utilisateur)
        elif self.tree.item(item, 'text') == 'Consoles':
            self.testFrame1_destroyChildren()
            SeeConsole(self.frame1, utilisateur)
        elif self.tree.item(item, 'text') == 'Gérer mes consoles':
            self.testFrame1_destroyChildren()
            AddConsole(self.frame1, utilisateur)

        elif self.tree.item(item, 'text') == 'Jeux':
            self.testFrame1_destroyChildren()
            SeeGame(self.frame1, utilisateur)
        elif self.tree.item(item, 'text') == 'Voir mes jeux':
            self.testFrame1_destroyChildren()
            SeeGame(self.frame1, utilisateur)
        elif self.tree.item(item, 'text') == 'Ajouter un jeu':
            self.testFrame1_destroyChildren()
            AddGame(self.frame1, utilisateur)
        elif self.tree.item(item, 'text') == 'Retirer un jeu':
            self.testFrame1_destroyChildren()

    def testFrame1_destroyChildren(self):
        """
        Will destroy all the children of self.frame1
        No parameters, no return
        """
        test = self.frame1.winfo_children()
        for i in test :
            i.destroy()