import tkinter

class HomepageAdmin :
    def __init__(self, fenetre, user):
        global f1
        f1 = fenetre
        #frameHomepage
        self.frameHomepage = tkinter.Frame(fenetre.window)
        self.frameHomepage.pack(side = 'left', fill ='y')
        self.label1 = tkinter.Label(self.frameHomepage, text = 'Pannel Administratif : ')
        self.label1.grid(row = 0, column = 0)
        self.label2 = tkinter.Label(self.frameHomepage, text = '')
        self.label2.grid(row = 1 , column = 0)
        self.boutonConsole = tkinter.Button(self.frameHomepage, text = 'Console',width = 20)
        self.boutonConsole.grid(row = 2, column = 0)
        self.boutonJeu = tkinter.Button(self.frameHomepage, text = 'Jeu', width = 20)
        self.boutonJeu.grid(row = 3, column = 0)
        self.boutonGenre = tkinter.Button(self.frameHomepage, text = 'Genre', width = 20)
        self.boutonGenre.grid(row = 4, column = 0)
        #frameCanva
        self.frame1 = tkinter.Frame(fenetre.window, bg ='grey50')
        self.frame1.pack(side = 'left', expand = 1, fill='both')
        self.canva = tkinter.Canvas(self.frame1, bg ='yellow')
        self.canva.pack(fill = 'both', expand = 1, pady = 2, padx = 2)