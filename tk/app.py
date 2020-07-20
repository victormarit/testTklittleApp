import tkinter as tk
from tk.connection import FrameConnection

class App :
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("650x400")
        self.window.minsize(600,350)
        self.interface = FrameConnection(self)
        self.window.mainloop()