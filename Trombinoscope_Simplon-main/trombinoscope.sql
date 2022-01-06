-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8081
-- Generation Time: Dec 18, 2021 at 10:25 AM
-- Server version: 5.7.24
-- PHP Version: 7.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `trombinoscope`
--

-- --------------------------------------------------------

--
-- Table structure for table `genres`
--

CREATE TABLE `genres` (
  `id_genre` int(11) NOT NULL,
  `genre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `genres`
--

INSERT INTO `genres` (`id_genre`, `genre`) VALUES
(1, 'M.'),
(2, 'Mme.'),
(3, 'Autre');

-- --------------------------------------------------------

--
-- Table structure for table `personnes`
--

CREATE TABLE `personnes` (
  `id_personne` int(11) NOT NULL,
  `nom_personne` varchar(50) NOT NULL,
  `prenom_personne` varchar(50) NOT NULL,
  `photo_personne` varchar(50) NOT NULL,
  `id_genre` int(11) NOT NULL,
  `id_statut` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `personnes`
--

INSERT INTO `personnes` (`id_personne`, `nom_personne`, `prenom_personne`, `photo_personne`, `id_genre`, `id_statut`) VALUES
(1, 'ADAM', 'Thierry', 'adam_thierry.jpg', 1, 4),
(2, 'BOREL', 'Bertrand', 'borel_bertrand.jpg', 1, 4),
(3, 'BOUCLY', 'Kévin', 'boucly_kevin.jpg', 1, 4),
(4, 'CORLAY', 'Morgan', 'corlay_morgan.jpg', 1, 4),
(5, 'COROLLER', 'Loïc', 'coroller_loic.jpg', 1, 4),
(6, 'DE SOUSA LUSTOSA SILVA', 'Lucas', 'de_sousa_lustosa_silva_lucas.jpg', 1, 4),
(7, 'FAUDEIL', 'Nathan', 'faudeil_nathan.jpg', 1, 4),
(8, 'GAVANCHA CASSIANO', 'Fabio', 'gavancha_cassiano_fabio.jpg', 1, 4),
(9, 'GUICHOUX', 'Quentin', 'guichoux_quentin.jpg', 1, 4),
(10, 'HELLER', 'Romain', 'heller_romain.jpg', 1, 4),
(11, 'IKHENECHE', 'Nacira', 'ikheneche_nacira.jpg', 2, 4),
(12, 'LANDURE', 'Pierre-Yves', 'landure_pierre_yves.jpg', 1, 4),
(13, 'LANNURIEN', 'Victor', 'lannurien_victor.jpg', 1, 4),
(14, 'LAXALDE', 'Ewen', 'laxalde_ewen.jpg', 1, 4),
(15, 'LE DEM', 'Maïna', 'le_dem_maina.jpg', 2, 4),
(16, 'LEPELLEY', 'Perrine', 'lepelley_perrine.jpg', 2, 4),
(17, 'LE ROCH', 'Gwenn', 'le_roch_gwenn.jpg', 1, 4),
(18, 'NAFOUSSI', 'Hichem', 'nafoussi_hichem.jpg', 1, 4),
(19, 'PENFEUNTEUN', 'Sylvia', 'penfeunteun_sylvia.jpg', 2, 4),
(20, 'PLESSIS', 'Loïc', 'plessis_loic.jpg', 1, 4),
(21, 'POIRIER', 'Hervé', 'poirier_herve.jpg', 1, 4),
(22, 'SANCHEZ', 'Pauline', 'sanchez_pauline.jpg', 2, 4),
(23, 'SEPHERI', 'Shima', 'sepheri_shima.jpg', 2, 4),
(24, 'TANGUY', 'Erwan', 'tanguy_erwan.jpg', 1, 4),
(25, 'TANGUY', 'Franky', 'tanguy_franky.jpg', 1, 4),
(26, 'JAMIN-NORMAND', 'Stéphane', 'jamin_normand_stephane.jpg', 1, 2),
(27, 'MOURCHID', 'Youssef', 'mourchid_youssef.jpg', 1, 2),
(28, 'KUSBERG', 'Tatiana', 'kusberg_tatiana.jpg', 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `statut`
--

CREATE TABLE `statut` (
  `id_statut` int(11) NOT NULL,
  `qualification_statut` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `statut`
--

INSERT INTO `statut` (`id_statut`, `qualification_statut`) VALUES
(1, 'Chargé de projet'),
(2, 'Formateur'),
(3, 'Etudiant P1'),
(4, 'Etudiant P2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `genres`
--
ALTER TABLE `genres`
  ADD PRIMARY KEY (`id_genre`);

--
-- Indexes for table `personnes`
--
ALTER TABLE `personnes`
  ADD PRIMARY KEY (`id_personne`),
  ADD KEY `id_genre` (`id_genre`),
  ADD KEY `id_statut` (`id_statut`);

--
-- Indexes for table `statut`
--
ALTER TABLE `statut`
  ADD PRIMARY KEY (`id_statut`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `genres`
--
ALTER TABLE `genres`
  MODIFY `id_genre` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `personnes`
--
ALTER TABLE `personnes`
  MODIFY `id_personne` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `statut`
--
ALTER TABLE `statut`
  MODIFY `id_statut` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `personnes`
--
ALTER TABLE `personnes`
  ADD CONSTRAINT `personnes_ibfk_1` FOREIGN KEY (`id_genre`) REFERENCES `genres` (`id_genre`),
  ADD CONSTRAINT `personnes_ibfk_2` FOREIGN KEY (`id_statut`) REFERENCES `statut` (`id_statut`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
