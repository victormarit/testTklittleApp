import tkinter
from tkinter import messagebox
from classes.db import DB

class SeeGame:
    def __init__(self, frame, user):
        self.frameApp = tkinter.Frame(frame)
        self.frameApp.pack(side = 'left', fill='both', expand=1)
        #
        self.secondFrame = tkinter.Frame(self.frameApp)
        self.secondFrame.pack(side = 'top', fill='both', expand= 1 )
        #
        self.items = []
        self.page()

    def page(self):
        if len(self.items) == 0:
            label = tkinter.Label(self.secondFrame, text = 'Pour le moment vous n\'avez pas de jeux')
            label.grid()
        