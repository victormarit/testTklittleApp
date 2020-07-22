import sys
sys.path.append('..')
from tkinter import ttk
import tkinter
from tkinter import PhotoImage

from tk.homepageAdminChoices.seeConsole import SeeConsole
from tk.homepageAdminChoices.addConsole import AddConsole
from tk.homepageAdminChoices.alterConsole import AlterConsole
from tk.homepageAdminChoices.delConsole import DelConsole
from tk.homepageAdminChoices.seeGenre import SeeGenre
from tk.homepageAdminChoices.addGenre import AddGenre
from tk.homepageAdminChoices.delGenre import DelGenre


class HomepageAdmin :
    def __init__(self, fenetre, user):
        global f1
        f1 = fenetre
        #frameHomepage
        self.frameHomepage = tkinter.Frame(fenetre.window, bg = 'white')
        self.frameHomepage.pack(side = 'left', fill ='y')
        #Label pannel admin
        self.labelWelcome = tkinter.Label(self.frameHomepage, text = 'Pannel Administratif', bg = 'white')
        self.labelWelcome.pack(padx = 20)
        #logoConsole
        self.logo = PhotoImage(file = 'img/logo/logoManette.gif').subsample(10, 10)
        #Widget treeview
        self.tree = ttk.Treeview(self.frameHomepage)
        self.tree.pack(expand = 1 , fill= 'both')
        #treeview_console
        self.console = self.tree.insert('', 0, text='Console', image = self.logo)
        self.tree.insert(self.console, 0,text='Ajouter une console', image = self.logo)
        self.tree.insert(self.console, 1,text='Modifier une console', image = self.logo)
        self.tree.insert(self.console, 2, text='Supprimer une console', image = self.logo)
        #treeview_genre
        self.genre = self.tree.insert('', 1, text='Genre')
        self.tree.insert(self.genre, 0, text='Ajouter un genre')
        self.tree.insert(self.genre, 1, text='Modifier un genre')
        self.tree.insert(self.genre, 2, text='Supprimer un genre')
        #find tree
        self.tree.bind("<Double-1>", self.onDoubleClick)
        #frameCanva
        self.frame1 = tkinter.Frame(fenetre.window)
        self.frame1.pack(side = 'left', expand = 1, fill='both')

    def onDoubleClick(self, event):
        item = self.tree.identify('item',event.x,event.y)
        if self.tree.item(item, 'text') == 'Console' :
            self.testFrame1_destroyChildren()
            SeeConsole(self.frame1)
        elif self.tree.item(item, 'text') == 'Ajouter une console': 
            self.testFrame1_destroyChildren()
            AddConsole(self.frame1)
        elif self.tree.item(item, 'text') == 'Modifier une console':
            self.testFrame1_destroyChildren()
            AlterConsole(self.frame1)
        elif self.tree.item(item, 'text') == 'Supprimer une console':
            self.testFrame1_destroyChildren()
            DelConsole(self.frame1)
        elif self.tree.item(item, 'text') == 'Genre':
            self.testFrame1_destroyChildren()
            SeeGenre(self.frame1)
        elif self.tree.item(item, 'text') == 'Ajouter un genre':
            self.testFrame1_destroyChildren()
            AddGenre(self.frame1)
        elif self.tree.item(item, 'text') == 'Modifier un genre':
            self.testFrame1_destroyChildren()
            #
        elif self.tree.item(item, 'text') == 'Supprimer un genre':
            self.testFrame1_destroyChildren()
            DelGenre(self.frame1)

        
    def testFrame1_destroyChildren(self):
        """
        Will destroy all the children of self.frame1
        No parameters, no return
        """
        test = self.frame1.winfo_children()
        for i in test :
            i.destroy()

