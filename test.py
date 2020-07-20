import tkinter as tk
import tkinter.ttk as ttk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.tree = ttk.Treeview()
        self.tree.pack()
        for i in range(10):
            self.tree.insert("", "end", iid = i ,text="Item %s" % i)
        self.tree.bind("<Double-1>", self.OnDoubleClick)
        self.root.mainloop()

    def OnDoubleClick(self, event):
        real_coords = (self.tree.winfo_pointerx() - self.tree.winfo_rootx(),
                       self.tree.winfo_pointery() - self.tree.winfo_rooty())
        item = self.tree.selection()[0]
        print(self.tree.get)

if __name__ == "__main__":
    app = App()