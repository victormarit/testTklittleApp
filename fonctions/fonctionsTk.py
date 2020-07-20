import tk.homepageAdmin
import tk.homepageUser

def adminOrClient(fenetre, utilisateur):
    if utilisateur.admin : 
        tk.homepageAdmin.HomepageAdmin(fenetre, utilisateur)
    else : 
        tk.homepageUser.HomepageUser(fenetre, utilisateur)