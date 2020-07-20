import sys
sys.path.append('..')
from tkinter import ttk
import tkinter
from tkinter import PhotoImage

class HomepageUser:
    def __init__(self, fenetre, user):
        global f1
        f1 = fenetre
        #frameHomepage
        self.frameHomepage = tkinter.Frame(fenetre.window)
        self.frameHomepage.pack(side = 'left', fill ='y')
        #logoConsole
        self.logo = PhotoImage(file = 'img/logo/logoManette.gif').subsample(10, 10)

        #Widget treeview
        self.tree = ttk.Treeview(self.frameHomepage)
        self.tree.pack(expand = 1 , fill= 'both')

        #treeview_console
        self.console = self.tree.insert('', 0, text='Consoles')
        self.tree.insert(self.console, 0, 'item1',text='Voir Mes Consoles', image = self.logo)
        self.tree.insert(self.console, 1, text='Supprimer Une console', image = self.logo)

        #treeview_genre
        self.genre = self.tree.insert('', 1, text='Jeu')
        self.tree.insert(self.genre, 0, text='Voir Mes Jeux')
        self.tree.insert(self.genre, 1, text='Supprimer un jeu')


        #find tree
        self.tree.bind("<Double-1>", self.onDoubleClick)

        #frameCanva

        self.frame1 = tkinter.Frame(fenetre.window, bg ='grey50')
        self.frame1.pack(side = 'left', expand = 1, fill='both')
        self.canva = tkinter.Canvas(self.frame1, bg ='yellow')
        self.canva.pack(fill = 'both', expand = 1, pady = 2, padx = 2)

    def onDoubleClick(self, event):
        item = self.tree.identify('item',event.x,event.y)
        print("you clicked on", self.tree.item(item, 'text'))
        if self.tree.item(item, 'text') == 'Voir Mes Consoles':
            self.canva.config(bg = 'red')