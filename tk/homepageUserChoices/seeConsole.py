import tkinter
from tkinter import messagebox
import classes.db

class SeeConsole:
    def __init__(self, frame):
        self.frameApp = tkinter.Frame(frame)
        self.frameApp.pack(side = 'left', fill='both', expand=1)
        #
        self.secondFrame = tkinter.Frame(self.frameApp, bg = 'red')
        self.secondFrame.pack(side = 'top', fill='both', expand= 1 )
        #
        self.lab = tkinter.Label(self.frameApp, text = 'test')