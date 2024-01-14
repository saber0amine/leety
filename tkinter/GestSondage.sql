-- Create database
CREATE DATABASE IF NOT EXISTS GestSondage;
USE GestSondage;

-- Drop foreign key constraints
ALTER TABLE Sujets DROP FOREIGN KEY Sujets_ibfk_1;

-- Drop existing tables
DROP TABLE IF EXISTS Votes;
DROP TABLE IF EXISTS Participants;
DROP TABLE IF EXISTS Sujets;
DROP TABLE IF EXISTS Sondages;

-- Create Sondages table
CREATE TABLE IF NOT EXISTS Sondages (
    numSo SMALLINT PRIMARY KEY,
    libelle VARCHAR(20),
    dateOuverture DATE,
    dateFermeture DATE
);

-- Create Sujets table
CREATE TABLE IF NOT EXISTS Sujets (
    numSu INT PRIMARY KEY,
    intitule VARCHAR(20),
    numSo SMALLINT,
    FOREIGN KEY (numSo) REFERENCES Sondages(numSo)
);

-- Create Participants table
CREATE TABLE IF NOT EXISTS Participants (
    numP INT PRIMARY KEY,
    nomPrenom VARCHAR(30),
    sexe BOOLEAN
);

-- Create Votes table
CREATE TABLE IF NOT EXISTS Votes (
    numV INT PRIMARY KEY,
    dateVote DATE,
    numP INT,
    numSu INT,
    choixVote CHAR(3),
    FOREIGN KEY (numP) REFERENCES Participants(numP),
    FOREIGN KEY (numSu) REFERENCES Sujets(numSu)
);

-- Sample data (you can insert actual data later)
INSERT INTO Sondages (numSo, libelle, dateOuverture, dateFermeture) VALUES
(1, 'Sondage1', '2024-01-01', '2024-01-10'),
(2, 'Sondage2', '2024-01-05', '2024-01-15');

INSERT INTO Sujets (numSu, intitule, numSo) VALUES
(1, 'Sujet1', 1),
(2, 'Sujet2', 1),
(3, 'Sujet3', 2);

INSERT INTO Participants (numP, nomPrenom, sexe) VALUES
(1, 'Participant1', 1),
(2, 'Participant2', 0),
(3, 'Participant3', 1);

INSERT INTO Votes (numV, dateVote, numP, numSu, choixVote) VALUES
(1, '2024-01-05', 1, 1, 'Oui'),
(2, '2024-01-06', 2, 1, 'Non'),
(3, '2024-01-07', 3, 1, 'Oui'),
(4, '2024-01-08', 1, 2, 'Non'),
(5, '2024-01-09', 2, 2, 'Oui'),
(6, '2024-01-10', 3, 2, 'Non');


-- Add more Sondages
INSERT INTO Sondages (numSo, libelle, dateOuverture, dateFermeture) VALUES
(3, 'Sondage3', '2024-01-15', '2024-01-25'),
(4, 'Sondage4', '2024-01-20', '2024-01-30');

-- Add more Sujets
INSERT INTO Sujets (numSu, intitule, numSo) VALUES
(4, 'Sujet4', 3),
(5, 'Sujet5', 3),
(6, 'Sujet6', 4);

-- Add more Participants
INSERT INTO Participants (numP, nomPrenom, sexe) VALUES
(4, 'Participant4', 0),
(5, 'Participant5', 1),
(6, 'Participant6', 0);

-- Add more Votes
INSERT INTO Votes (numV, dateVote, numP, numSu, choixVote) VALUES
(7, '2024-01-20', 4, 4, 'Oui'),
(8, '2024-01-21', 5, 4, 'Non'),
(9, '2024-01-22', 6, 4, 'Oui'),
(10, '2024-01-23', 4, 5, 'Non'),
(11, '2024-01-24', 5, 5, 'Oui'),
(12, '2024-01-25', 6, 5, 'Non');
