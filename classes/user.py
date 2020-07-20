class User :
    def __init__(self, data):
        self.id = data[0]
        self.nom = data[1]
        self.prenom = data[2]
        self.email = data[3]
        self.password = data[4]
        self.admin = data[5]
        self.auth = True
        