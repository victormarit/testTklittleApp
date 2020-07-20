import tk.homepageAdmin
import tk.homepageUser
import hashlib

def adminOrClient(fenetre, utilisateur):
    if utilisateur.admin : 
        tk.homepageAdmin.HomepageAdmin(fenetre, utilisateur)
    else : 
        tk.homepageUser.HomepageUser(fenetre, utilisateur)

def hashPassword(password):
    """
    Allows you to hash a password
    Param : password(type) - string
    Return : pw(type) - string ; length : 40 
    """
    pw = hashlib.sha1(password.encode())
    pw = pw.hexdigest()
    return pw