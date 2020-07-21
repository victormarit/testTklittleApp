import tkinter
from tk.homepageAdminChoices.seeGenre import SeeGenre

class AddGenre:
    def __init__(self, frame):
        global mainFrame
        mainFrame = frame
        self.frameApp = tkinter.Frame(frame, bg ='grey50')
        self.frameApp.pack()
        #
        self.labelWelcome = tkinter.Label(self.frameApp, text = 'Ajouter un Genre')
        self.labelWelcome.grid(row = 0, column = 0, columnspan = 2)
        #
        self.labelVoid1 = tkinter.Label(self.frameApp, text = '')
        self.labelVoid1.grid(row = 1, column = 0)
        #
        self.name = tkinter.Label(self.frameApp, text = 'Nom Genre : ')
        self.name.grid(row = 2, column = 0)
        self.nameEntry = tkinter.Entry(self.frameApp)
        self.nameEntry.grid(row = 2, column = 1)
        #logo
        self.logo = tkinter.Label(self.frameApp, text = 'Lien Vers Logo : ')
        self.logo.grid(row = 3, column = 0 )
        self.logoEntry = tkinter.Entry(self.frameApp)
        self.logoEntry.grid(row = 3, column = 1 )
        #void
        self.labelVoid2 = tkinter.Label(self.frameApp, text = '')
        self.labelVoid2.grid(row = 4, column = 0)
        #valider
        self.boutonValider = tkinter.Button(self.frameApp, text = 'Valider', width = 10)
        self.boutonValider.grid(row = 5, column = 0, columnspan = 2, pady= 5)
        #Annuler
        self.boutonAnnuler = tkinter.Button(self.frameApp, text = 'Annuler', width = 10, command = self.cancel)
        self.boutonAnnuler.grid(row = 6, column = 0, columnspan = 2)

    def cancel(self):
        self.frameApp.destroy()
        SeeGenre(mainFrame)