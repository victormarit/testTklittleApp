import tk.homepageAdmin
import tk.homepageUser
import hashlib
import tkinter

def adminOrClient(fenetre, utilisateur):
    menuTK(fenetre)
    if utilisateur.admin : 
        tk.homepageAdmin.HomepageAdmin(fenetre, utilisateur)
    else : 
        tk.homepageUser.HomepageUser(fenetre, utilisateur)

def menuTK(f1):
    mainMenu=tkinter.Menu(f1.window)
    first_menu=tkinter.Menu(mainMenu,tearoff=0)
    first_menu.add_command(label="Option1")
    first_menu.add_command(label="NewWindow")
    first_menu.add_separator()
    first_menu.add_command(label="Quitter",command=f1.window.quit)
    second_menu=tkinter.Menu(mainMenu)
    second_menu.add_command(label="commande1")
    second_menu.add_command(label="commande2")
    second_menu.add_command(label="commande3")
    mainMenu.add_cascade(label="Premier",menu=first_menu)
    mainMenu.add_cascade(label="Second",menu=second_menu)
    f1.window.config(menu=mainMenu)


def hashPassword(password):
    """
    Allows you to hash a password
    Param : password(type) - string
    Return : pw(type) - string ; length : 40 
    """
    pw = hashlib.sha1(password.encode())
    pw = pw.hexdigest()
    return pw

