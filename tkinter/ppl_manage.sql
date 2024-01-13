--
-- Base de données: `gestionpersonnes`
--

-- --------------------------------------------------------

--
-- Structure de la table `profil`
--
DROP TABLE IF EXISTS `personne`;
DROP TABLE IF EXISTS `profil`;

CREATE TABLE `profil` (
  `id` varchar(10) NOT NULL,
  `libelle` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;

--
-- Structure de la table `personne`
--

CREATE TABLE IF NOT EXISTS `personne` (
  `id` varchar(10) NOT NULL,
  `nomPrenom` varchar(30) NOT NULL,
  `sexe` varchar(10) NOT NULL,
  `dateNaiss` varchar(10) NOT NULL,
  `email` varchar(30) NOT NULL,
  `idProfil` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nomPrenom` (`nomPrenom`,`email`),
  KEY `idProfil` (`idProfil`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


ALTER TABLE `personne`
  ADD CONSTRAINT `personne_ibfk_1` FOREIGN KEY (`idProfil`) REFERENCES `profil` (`id`);



