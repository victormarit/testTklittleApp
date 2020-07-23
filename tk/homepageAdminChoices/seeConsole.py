import tkinter
from tkinter import messagebox
import classes.db

class SeeConsole:
    def __init__(self, frame):
        self.frameApp = tkinter.Frame(frame)
        self.frameApp.pack(side = 'left', fill='both', expand=1)
        #
        self.secondFrame = tkinter.Frame(self.frameApp)
        self.secondFrame.pack(side = 'top', fill='both', expand= 1 )
        #
        self.db = classes.db.DB()
        self.data = self.db.findConsoles()
        self.seeAllItem()
    
    def seeAllItem(self):
        if self.data is None:
            messagebox.showinfo("Echec",'Connexion à la base de données perdue')
        elif len(self.data) == 0 : 
            self.label = tkinter.Label(self.secondFrame, text = 'Aucune console de jeux trouvée dans la BDD')
            self.label.grid(row = 1, column = 1)
        else: 
            i = 1
            y = 2
            lab = tkinter.Label(self.secondFrame, text = 'Toutes les consoles')
            lab.grid(row = 0, column = 0, columnspan = 5, padx = 10)
            for genre in self.data : 
                if i >4:
                    i=1
                    y+=1     
                label = tkinter.Label(self.secondFrame, text = genre[1])
                label.grid(row = y, column = i, pady = 10, padx = 10)
                i+=1
