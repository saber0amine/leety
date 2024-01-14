-- Drop tables if they exist
DROP TABLE IF EXISTS `personne`;
DROP TABLE IF EXISTS `profil`;

-- Create `profil` table with auto-increment primary key
CREATE TABLE `profil` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `libelle` VARCHAR(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Create `personne` table with auto-increment primary key
CREATE TABLE IF NOT EXISTS `personne` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `nomPrenom` VARCHAR(30) NOT NULL,
  `sexe` VARCHAR(10) NOT NULL,
  `dateNaiss` VARCHAR(10) NOT NULL,
  `email` VARCHAR(30) NOT NULL,
  `idProfil` INT NOT NULL,
  UNIQUE KEY `nomPrenom` (`nomPrenom`, `email`),
  KEY `idProfil` (`idProfil`),
  CONSTRAINT `personne_ibfk_1` FOREIGN KEY (`idProfil`) REFERENCES `profil` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



-- Insert a new profil
INSERT INTO `profil` (`libelle`) VALUES ('Some Libelle');

-- Insert a new personne referencing the above profil
INSERT INTO `personne` (`nomPrenom`, `sexe`, `dateNaiss`, `email`, `idProfil`) 
VALUES ('John Doe', 'Masculin', '2000-01-01', 'john.doe@example.com', LAST_INSERT_ID());


SELECT * FROM profil ; 