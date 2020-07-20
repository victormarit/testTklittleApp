import tkinter

class MenuTK:
    def __init__(self, f1):
        self.mainMenu=tkinter.Menu(f1.window)
        self.first_menu=tkinter.Menu(self.mainMenu, tearoff=0)
        self.first_menu.add_command(label="Option1")
        self.first_menu.add_command(label="NewWindow")
        self.first_menu.add_separator()
        self.first_menu.add_command(label="Quitter",command=f1.window.quit)
        self.second_menu=tkinter.Menu(self.mainMenu)
        self.second_menu.add_command(label="commande1")
        self.second_menu.add_command(label="commande2")
        self.second_menu.add_command(label="commande3")
        self.mainMenu.add_cascade(label="Premier",menu=self.first_menu)
        self.mainMenu.add_cascade(label="Second",menu=self.second_menu)
        f1.window.config(menu = self.mainMenu)