-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 16, 2024 at 04:22 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `airline_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `airline`
--

CREATE TABLE `airline` (
  `name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `airline_staff`
--

CREATE TABLE `airline_staff` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `first_name` varchar(15) NOT NULL,
  `last_name` varchar(15) NOT NULL,
  `date_of_birth` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `airline_staff_email_address`
--

CREATE TABLE `airline_staff_email_address` (
  `username` varchar(20) NOT NULL,
  `email_address` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `airline_staff_phone_number`
--

CREATE TABLE `airline_staff_phone_number` (
  `username` varchar(20) NOT NULL,
  `phone_number` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `airplane`
--

CREATE TABLE `airplane` (
  `airline_name` varchar(20) NOT NULL,
  `id_number` varchar(20) NOT NULL,
  `maintenance_id` varchar(20) DEFAULT NULL,
  `num_of_seat` int(11) NOT NULL,
  `manufacturing_company` varchar(20) NOT NULL,
  `model_number` varchar(20) NOT NULL,
  `manufacturing_date` date NOT NULL,
  `age` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `airport`
--

CREATE TABLE `airport` (
  `code` decimal(5,0) NOT NULL,
  `name` varchar(15) NOT NULL,
  `city` varchar(15) NOT NULL,
  `country` varchar(15) NOT NULL,
  `number_of_terminals` decimal(8,0) NOT NULL,
  `type` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `email_address` varchar(30) NOT NULL,
  `first_name` varchar(15) NOT NULL,
  `last_name` varchar(15) NOT NULL,
  `password` varchar(20) NOT NULL,
  `building_number` int(11) NOT NULL,
  `street` varchar(20) NOT NULL,
  `apt_number` int(11) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `zipcode` int(11) NOT NULL,
  `passport_number` varchar(10) NOT NULL,
  `passport_expiration` date NOT NULL,
  `passport_country` varchar(20) NOT NULL,
  `date_of_birth` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `customerphone`
--

CREATE TABLE `customerphone` (
  `email_address` varchar(30) NOT NULL,
  `phone_number` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `employed_by`
--

CREATE TABLE `employed_by` (
  `airline_name` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `flight`
--

CREATE TABLE `flight` (
  `airline_name` varchar(20) NOT NULL,
  `flight_number` varchar(5) NOT NULL,
  `depart_date` date NOT NULL,
  `depart_time` time NOT NULL,
  `depart_airport_code` decimal(5,0) NOT NULL,
  `arrival_date` date NOT NULL,
  `arrival_time` time NOT NULL,
  `arrival_airport_code` decimal(5,0) NOT NULL,
  `base_price` decimal(5,2) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `maintenance`
--

CREATE TABLE `maintenance` (
  `id` varchar(20) NOT NULL,
  `start_date` date NOT NULL,
  `start_time` time NOT NULL,
  `end_date` date NOT NULL,
  `end_time` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `purchase`
--

CREATE TABLE `purchase` (
  `id_number` varchar(20) NOT NULL,
  `email_address` varchar(30) NOT NULL,
  `purchase_time` time NOT NULL,
  `purchase_date` date NOT NULL,
  `card_type` varchar(30) NOT NULL,
  `card_number` varchar(30) NOT NULL,
  `name_on_card` varchar(20) NOT NULL,
  `expiration_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `reviews`
--

CREATE TABLE `reviews` (
  `email_address` varchar(20) NOT NULL,
  `airline_name` varchar(20) NOT NULL,
  `flight_number` varchar(5) NOT NULL,
  `depart_date` date NOT NULL,
  `depart_time` time NOT NULL,
  `rating` decimal(2,1) NOT NULL,
  `comment` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ticket`
--

CREATE TABLE `ticket` (
  `id_number` varchar(20) NOT NULL,
  `airline_name` varchar(20) NOT NULL,
  `flight_number` varchar(5) NOT NULL,
  `depart_date` date NOT NULL,
  `depart_time` time NOT NULL,
  `sold_price` decimal(5,2) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `date_of_birth` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `airline`
--
ALTER TABLE `airline`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `airline_staff`
--
ALTER TABLE `airline_staff`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `airline_staff_email_address`
--
ALTER TABLE `airline_staff_email_address`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `airline_staff_phone_number`
--
ALTER TABLE `airline_staff_phone_number`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `airplane`
--
ALTER TABLE `airplane`
  ADD PRIMARY KEY (`airline_name`,`id_number`),
  ADD KEY `maintenance_id` (`maintenance_id`);

--
-- Indexes for table `airport`
--
ALTER TABLE `airport`
  ADD PRIMARY KEY (`code`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`email_address`);

--
-- Indexes for table `customerphone`
--
ALTER TABLE `customerphone`
  ADD PRIMARY KEY (`email_address`,`phone_number`);

--
-- Indexes for table `employed_by`
--
ALTER TABLE `employed_by`
  ADD PRIMARY KEY (`airline_name`,`username`),
  ADD KEY `username` (`username`);

--
-- Indexes for table `flight`
--
ALTER TABLE `flight`
  ADD PRIMARY KEY (`airline_name`,`flight_number`,`depart_date`,`depart_time`),
  ADD KEY `depart_airport_code` (`depart_airport_code`),
  ADD KEY `arrival_airport_code` (`arrival_airport_code`);

--
-- Indexes for table `maintenance`
--
ALTER TABLE `maintenance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `purchase`
--
ALTER TABLE `purchase`
  ADD PRIMARY KEY (`id_number`,`email_address`),
  ADD KEY `email_address` (`email_address`);

--
-- Indexes for table `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`email_address`,`airline_name`,`flight_number`,`depart_date`,`depart_time`),
  ADD KEY `airline_name` (`airline_name`,`flight_number`,`depart_date`,`depart_time`);

--
-- Indexes for table `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`id_number`),
  ADD KEY `airline_name` (`airline_name`,`flight_number`,`depart_date`,`depart_time`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `airline_staff_email_address`
--
ALTER TABLE `airline_staff_email_address`
  ADD CONSTRAINT `airline_staff_email_address_ibfk_1` FOREIGN KEY (`username`) REFERENCES `airline_staff` (`username`);

--
-- Constraints for table `airline_staff_phone_number`
--
ALTER TABLE `airline_staff_phone_number`
  ADD CONSTRAINT `airline_staff_phone_number_ibfk_1` FOREIGN KEY (`username`) REFERENCES `airline_staff` (`username`);

--
-- Constraints for table `airplane`
--
ALTER TABLE `airplane`
  ADD CONSTRAINT `airplane_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`name`),
  ADD CONSTRAINT `airplane_ibfk_2` FOREIGN KEY (`maintenance_id`) REFERENCES `maintenance` (`id`);

--
-- Constraints for table `customerphone`
--
ALTER TABLE `customerphone`
  ADD CONSTRAINT `customerphone_ibfk_1` FOREIGN KEY (`email_address`) REFERENCES `customer` (`email_address`);

--
-- Constraints for table `employed_by`
--
ALTER TABLE `employed_by`
  ADD CONSTRAINT `employed_by_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`name`),
  ADD CONSTRAINT `employed_by_ibfk_2` FOREIGN KEY (`username`) REFERENCES `airline_staff` (`username`);

--
-- Constraints for table `flight`
--
ALTER TABLE `flight`
  ADD CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`depart_airport_code`) REFERENCES `airport` (`code`),
  ADD CONSTRAINT `flight_ibfk_2` FOREIGN KEY (`arrival_airport_code`) REFERENCES `airport` (`code`),
  ADD CONSTRAINT `flight_ibfk_3` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`name`);

--
-- Constraints for table `purchase`
--
ALTER TABLE `purchase`
  ADD CONSTRAINT `purchase_ibfk_1` FOREIGN KEY (`id_number`) REFERENCES `ticket` (`id_number`),
  ADD CONSTRAINT `purchase_ibfk_2` FOREIGN KEY (`email_address`) REFERENCES `customer` (`email_address`);

--
-- Constraints for table `reviews`
--
ALTER TABLE `reviews`
  ADD CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`airline_name`,`flight_number`,`depart_date`,`depart_time`) REFERENCES `flight` (`airline_name`, `flight_number`, `depart_date`, `depart_time`),
  ADD CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`email_address`) REFERENCES `customer` (`email_address`);

--
-- Constraints for table `ticket`
--
ALTER TABLE `ticket`
  ADD CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`airline_name`,`flight_number`,`depart_date`,`depart_time`) REFERENCES `flight` (`airline_name`, `flight_number`, `depart_date`, `depart_time`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
