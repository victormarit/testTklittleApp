import tkinter 
from tkinter import messagebox
from fonctions.fonctionsTk import hashPassword
from classes.db import DB

class UpdateUserPassword: 
    def __init__(self, utilisateur, frame):
        global frame1
        global user 
        user = utilisateur
        frame1 = frame

        self.frameApp = tkinter.Frame(frame)
        self.frameApp.pack()

        self.labelWelcome = tkinter.Label(self.frameApp, text = 'Modifier mot de passe')
        self.labelWelcome.grid(row = 0, column = 0, columnspan = 2)
        self.void = tkinter.Label(self.frameApp, text = '')
        self.void.grid(row=1, column=0)

        self.oldPw = tkinter.Label(self.frameApp, text = 'Ancien de mot de passe : ')
        self.oldPw.grid(row = 2, column = 0)
        self.oldPwEntry = tkinter.Entry(self.frameApp, show = '*')
        self.oldPwEntry.grid(row = 2, column = 1)

        self.newPw = tkinter.Label(self.frameApp, text = 'Nouveau mot de passe : ')
        self.newPw.grid(row = 3, column = 0)
        self.newPwEntry = tkinter.Entry(self.frameApp, show ='*')
        self.newPwEntry.grid(row = 3, column = 1)

        self.newPwConfirm = tkinter.Label(self.frameApp, text = 'Confirmer mot de passe : ')
        self.newPwConfirm.grid(row = 4, column = 0)
        self.newPwConfirmEntry = tkinter.Entry(self.frameApp, show ="*")
        self.newPwConfirmEntry.grid(row = 4, column = 1)

        self.buttonModifier = tkinter.Button(self.frameApp, text = "Modifier", width = 10, command = self.modifier)
        self.buttonModifier.grid(row = 5, column = 0, columnspan = 2,  pady = 5)
        self.buttonAnnuler = tkinter.Button(self.frameApp, text = "Annuler", width = 10, command = self.annuler)
        self.buttonAnnuler.grid(row = 6, column = 0, columnspan = 2)

    def annuler(self):
        widget = frame1.winfo_children()
        for i in widget : 
            i.destroy()

    def modifier(self) : 
        if self.oldPwEntry.get() != '' and self.newPwEntry.get() != '' and self.newPwConfirmEntry.get() != "":
            if self.newPwEntry.get() == self.newPwConfirmEntry.get():
                test = self.testOldPassword()
                if test : 
                    testBis = messagebox.askokcancel('Valider', 'Etes vous sur de vouloir modifier votre mot de passe')
                    if testBis:
                        newPassword = hashPassword( self.newPwEntry.get() )
                        self.updateUserPW(newPassword)
                        self.changePWInDB(newPassword)
                        messagebox.showinfo('Modification', 'Vos données ont été mises à jour')
                        self.annuler()
                else : 
                    messagebox.showinfo('Erreur', 'L\'ancien mot de passe est faux')
            else : 
                messagebox.showinfo('Erreur', 'Erreur lors de la confirmation du nouveau mot de passe')
        else : 
            messagebox.showinfo('Erreur', 'Veuillez remplir tous les champs')
    
    def testOldPassword(self):
        pw = hashPassword(self.oldPwEntry.get())
        if pw == user.password:
            return True
        else :
            return False

    def updateUserPW(self, pw):
        user.changePW(pw)

    def changePWInDB(self, pw):
        info = (pw, user.id)
        bdd = DB()
        bdd.updateUserPasswordDB(info)