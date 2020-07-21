import tkinter

class SeeGenre:
    def __init__(self, frame):
        self.frameApp = tkinter.Frame(frame, bg ='grey50')
        self.frameApp.pack(side = 'left', fill='x', expand=1)
        self.label = tkinter.Label(self.frameApp, text = 'Pas de genre')
        self.label.pack()