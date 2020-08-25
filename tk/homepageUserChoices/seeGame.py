import tkinter
from tkinter import ttk
from tkinter import messagebox
from classes.testNewDBConnection.dbGame import DbGame

class SeeGame:
    def __init__(self, frame, user):
        self.user = user
        self.frame = frame
        self.frameApp = tkinter.Frame(self.frame)
        self.frameApp.pack()
        #
        self.listGames = []
        self.getGamecollectionInfo()
        self.page()
    
    def getGamecollectionInfo(self):
        db = DbGame()
        self.listGames = db.getUserCollectionGame((self.user.id,))

    def page(self):
        if len(self.listGames) > 0 :
            global treeview
            welcomeLabel = tkinter.Label(self.frameApp, text = 'Vos jeux')
            welcomeLabel.grid(row = 0 , column = 0, pady = 10)
            scrollbar = tkinter.Scrollbar(self.frameApp)
            treeview = ttk.Treeview(self.frameApp) 
            treeview['columns'] = ('#1', '#2')
            treeview.grid(row = 1, column = 0)  
            treeview.column('#0', width=200, minwidth = 200, stretch= tkinter.NO)
            treeview.heading('#0', text="Jeu(x)")
            treeview.column('#1', width=70, minwidth = 70, stretch= tkinter.NO)
            treeview.heading('#1', text="Quantité")
            treeview.column('#2', width=70, minwidth = 70, stretch= tkinter.NO)
            treeview.heading('#2', text="Etat")
            for game in self.listGames:
                if game[2] == 0 :
                    stat = 'A faire'
                else :
                    stat = 'Fait'
                treeview.insert('', 'end', text = game[0], values = (game[1], stat))
            scrollbar.grid(row = 1, column = 1, sticky = 'ns')
            scrollbar.config( command = treeview.yview )
            updateButton = tkinter.Button(self.frameApp, text = 'Modifier', width = 15, command = self.updateGame)
            updateButton.grid(row = 2, column = 0, pady = 5)
            delete = tkinter.Button(self.frameApp, text = 'Supprimer', width = 15, command = self.delGame)
            delete.grid(row = 3, column = 0) 
        else : 
            label = tkinter.Label(self.frameApp, text = 'Vous n\'avez pas de jeu')
            label.grid()
        
    def testvalue(self):
        try : 
            curItem = treeview.focus()
            name = (treeview.item(curItem)['text'],)
            if name[0] == '':
                raise ValueError
            return True
        except ValueError:
            messagebox.showerror('Erreur', 'Veuillez sélectionner un jeu')
            return False
            
    def delGame(self) : 
        boolean = self.testvalue()
        if boolean :
            test = messagebox.askokcancel('Supprimer', 'Etes vous sur de vouloir supprimer ce jeu de votre collection')
            if test : 
                curItem = treeview.focus()
                name = (treeview.item(curItem)['text'],)
                db = DbGame()
                id = db.getGameId(name)
                informations = (self.user.id, id[0])
                db.delOneGameInCollection(informations)
                self.frameApp.destroy()
                SeeGame(self.frame, self.user)

    def updateGame(self):
        boolean = self.testvalue()
        if boolean : 
            global quantityEntry
            global radio1
            global radio2
            global var
            global name
            var = tkinter.IntVar()
            test = messagebox.askokcancel('Modifer', 'Voulez-vous modifier les informations de ce jeux')
            if test:
                curItem = treeview.focus()
                name = (treeview.item(curItem)['text'],)
                number = treeview.item(curItem)['values'][0]
                widgets = self.frameApp.winfo_children()
                for widget in widgets:
                    widget.destroy()
                welcomeLabel = tkinter.Label(self.frameApp, text = 'Modifier : ' + name[0])
                welcomeLabel.grid(row = 0, column = 0, columnspan = 2)
                void = tkinter.Label(self.frameApp, text = '')
                void.grid(row = 1, column = 0)
                quantity = tkinter.Label(self.frameApp, text ='Quantité possédé :')
                quantity.grid(row = 2, column = 0 )
                quantityEntry = tkinter.Entry(self.frameApp)
                quantityEntry.insert(1, number)
                quantityEntry.grid(row = 2, column = 1)
                radio1 = tkinter.Radiobutton(self.frameApp, variable= var ,text = 'A faire', value = 0)
                radio1.grid(row = 3, column = 0, columnspan = 2)
                radio2 = tkinter.Radiobutton(self.frameApp, text ='  Fini   ',variable = var, value = 1)
                radio2.grid(row = 4, column = 0, columnspan = 2)
                cancel = tkinter.Button(self.frameApp, text = 'Annuler', width = 15, command = self.cancelUpdateGame)
                cancel.grid(row = 5, column = 0, columnspan = 2, pady = 5)
                update = tkinter.Button(self.frameApp, text = 'Modifier', width = 15, command = self.saveUpdateGameCollection)
                update.grid(row = 6, column = 0, columnspan = 2)
    
    def cancelUpdateGame(self) : 
        self.frameApp.destroy()
        SeeGame(self.frame, self.user)
    
    def saveUpdateGameCollection(self):
        test = messagebox.askokcancel('Valider', 'Voulez-vous modifier ce jeux')
        if test :
            try :
                nb = int(quantityEntry.get())
                if nb > 0 : 
                    database = DbGame()
                    idGame = database.getGameId(name)
                    info = (nb, var.get(), self.user.id ,idGame[0])
                    print(info)
                    database.updateOneGameInCollection(info)
                    self.cancelUpdateGame()
                else : 
                    raise ValueError
            except ValueError:
                messagebox.showerror('Erreur', 'La quantité possédée devrait être un entier positif supérieur à 0')