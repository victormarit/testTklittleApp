---Création de la BDD---

CREATE DATABASE testCollecDB1;

---Création des tables---

CREATE TABLE user 
(
    idUser int PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    pw VARCHAR(50) NOT NULL,
    admin BOOLEAN NOT NULL DEFAULT FALSE
) ENGINE=InnoDB ;

CREATE TABLE genre(
   idGenre INT PRIMARY KEY AUTO_INCREMENT,
   nomGenre VARCHAR(50) NOT NULL UNIQUE
) ENGINE=InnoDB;


CREATE TABLE console(
   idConsole INT PRIMARY KEY AUTO_INCREMENT,
   Nom VARCHAR(50) NOT NULL UNIQUE,
   Constructeur VARCHAR(50) NOT NULL,
   logo VARCHAR(50),
   annee INT NOT NULL
) ENGINE=InnoDB;

CREATE TABLE possessionConsole(
    idUser INT,
    idConsole INT,
    nb INT NOT NULL,
    PRIMARY KEY (idUser, idConsole),
    FOREIGN KEY(idUser) REFERENCES user(idUser),
    FOREIGN KEY(idConsole) REFERENCES console(idConsole)

) ENGINE=InnoDB;

CREATE TABLE jeu(
   idJeu INT PRIMARY KEY AUTO_INCREMENT,
   Nom VARCHAR(50) NOT NULL,
   pegi INT,
   idGenre INT NOT NULL,
   idConsole INT NOT NULL,
   FOREIGN KEY(idGenre) REFERENCES Genre(idGenre),
   FOREIGN KEY(idConsole) REFERENCES Console(idConsole)
)ENGINE=InnoDB;

CREATE TABLE gameCollection(
   idUser INT,
   idJeu INT,
   nb INT,
   PRIMARY KEY(idUser, idJeu),
   FOREIGN KEY(idUser) REFERENCES user(idUser),
   FOREIGN KEY(idJeu) REFERENCES jeu(idJeu)
)ENGINE=InnoDB;






---Insertion de valeurs---
INSERT INTO user (`nom`, `prenom`, `email`, `pw`, `admin`) VALUES ('Marit', 'Victor', 'victormarit.95@gmail.com', 'cc6511246b39e5cca492c3f945cdebe4fcea0052', '1');