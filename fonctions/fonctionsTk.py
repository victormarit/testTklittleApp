import hashlib

def hashPassword(password):
    """
    Allows you to hash a password
    Param : password(type) - string
    Return : pw(type) - string ; length : 40 
    """
    pw = hashlib.sha1(password.encode())
    pw = pw.hexdigest()
    return pw

