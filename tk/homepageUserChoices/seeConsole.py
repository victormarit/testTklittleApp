import tkinter
from tkinter import messagebox
from classes.db import DB

class SeeConsole:
    def __init__(self, frame, user):
        self.frameApp = tkinter.Frame(frame)
        self.frameApp.pack(side = 'left', fill='both', expand=1)
        #
        self.secondFrame = tkinter.Frame(self.frameApp)
        self.secondFrame.pack(side = 'top', fill='both', expand= 1 )
        #
        self.db = DB()
        self.data = self.db.userConsoleCollection((user.id,))
        self.seeAllItem()

    def seeAllItem(self):
        print(self.data)
        if self.data is None:
            messagebox.showinfo("Echec",'Connexion à la base de données perdue')
        elif len(self.data) == 0 : 
            self.label = tkinter.Label(self.secondFrame, text = 'Vous n\'avez pour le moment aucune console de jeux')
            self.label.grid(row = 0, column = 0)
        else: 
            i = 1
            y = 2
            lab = tkinter.Label(self.secondFrame, text = 'Vos consoles')
            lab.grid(row = 0, column = 0, columnspan = 5, padx = 10)
            for (nom, nb) in self.data : 
                if i >4:
                    i=1
                    y+=1     
                label = tkinter.Label(self.secondFrame, text = nom + '\nQuantité : ' + str(nb))
                label.grid(row = y, column = i, pady = 10, padx = 10)
                i+=1