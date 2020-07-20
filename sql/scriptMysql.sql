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
);

CREATE TABLE Console(
   idConsole INT PRIMARY KEY AUTO_INCREMENT,
   Nom VARCHAR(50) NOT NULL UNIQUE,
   Constructeur VARCHAR(50) NOT NULL
);


---Insertion de valeurs---
INSERT INTO user (`nom`, `prenom`, `email`, `pw`, `admin`) VALUES ('Marit', 'Victor', 'victormarit.95@gmail.com', 'cc6511246b39e5cca492c3f945cdebe4fcea0052', '1');