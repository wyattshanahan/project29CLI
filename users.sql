-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 17, 2022 at 06:34 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

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
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `userID` int(255) NOT NULL,
  `fname` varchar(999) NOT NULL,
  `lname` varchar(999) NOT NULL,
  `street` varchar(999) NOT NULL,
  `city` varchar(999) NOT NULL,
  `state` varchar(999) NOT NULL,
  `userZip` varchar(999) NOT NULL,
  `username` varchar(999) NOT NULL,
  `password` varchar(999) NOT NULL,
  `email` varchar(999) NOT NULL,
  `telephone` varchar(999) NOT NULL,
  `cardNum` varchar(999) NOT NULL,
  `cvv` int(255) NOT NULL,
  `cardName` varchar(999) NOT NULL,
  `cardDate` varchar(999) NOT NULL,
  `orderNum` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userID`, `fname`, `lname`, `street`, `city`, `state`, `userZip`, `username`, `password`, `email`, `telephone`, `cardNum`, `cvv`, `cardName`, `cardDate`, `orderNum`) VALUES
(0, 'Jack', 'Pistachio', '12 MS 12-W', 'Ackerman', 'MS', '39738', 'Jpistachio', 'bigCooli0', 'jackpistachio292@gmail.com', '662-361-0428', '1239203847289172', 122, 'Jack Pistachio', '11/2012', 0),
(0, 'Neil', 'Yakapov', '237 91st Street', 'Edmonton', 'AB', 'T6E 2Z7', 'nyakapov', 'pAsSwOrD!', 'nyakapov@nhl.com', '627-232-1242', '1212646423234232', 134, 'Neil Yakapov', '12/2022', 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
