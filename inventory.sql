-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 29, 2022 at 09:00 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project29`
--

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `Title` text NOT NULL,
  `Developer` text NOT NULL,
  `Release Year` text NOT NULL,
  `Console` text NOT NULL,
  `GameID` text NOT NULL,
  `Price` text NOT NULL,
  `Quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`Title`, `Developer`, `Release Year`, `Console`, `GameID`, `Price`, `Quantity`) VALUES
('Halo: Combat Evolved', '343 Industries', '2001', 'Xbox', '1063', '$60', 8),
('Pokemon FireRed', 'Nintendo', '2004', 'Gameboy Advance', '1084', '$60', 9),
('Fallout 3', 'Bethesda Softworks', '2008', 'Xbox 360', '1027', '$20', 7),
('World of Warcraft', 'Blizzard Entertainment', '2004', 'PC', '1072', '$10', 8),
('Final Fantasy XII', 'Square Enix', '2006', 'Playstation 4', '1059', '$20', 8),
('Super Mario Odyssey ', 'Nintendo', '2017', 'Switch', '1046', '$60', 7),
('GoldenEye 007', 'Rare', '1997', 'Nintendo 64', '1013', '$30', 9),
('Madden NFL 2003', 'EA Tiburon', '2002', 'Playstation 2', '1039', '$10', 7),
('BioShock', 'Irrational Games', '2008', 'Playstation 3', '1002', '$10', 8),
('Call of Duty 4: Modern Warfare', 'Infinity Ward', '2007', 'Xbox 360', '1098', '$60', 7),
('Batman: Arkham City', 'Rocksteady Studios', '2011', 'Xbox 360', '1077', '$50', 8),
('God of War', 'Santa Monica Studio', '2018', 'Playstation 4', '1054', '$50', 9);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
