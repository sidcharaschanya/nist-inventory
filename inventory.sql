-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 15, 2021 at 07:52 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.1.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inventory`
--

-- --------------------------------------------------------

--
-- Table structure for table `algae`
--

CREATE TABLE `algae` (
  `id` int(10) NOT NULL,
  `name` varchar(300) DEFAULT NULL,
  `agar` varchar(300) DEFAULT NULL,
  `temperature` varchar(100) DEFAULT NULL,
  `storage` varchar(100) DEFAULT NULL,
  `remarks` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `algae`
--

INSERT INTO `algae` (`id`, `name`, `agar`, `temperature`, `storage`, `remarks`) VALUES
(1, 'Spirulina ', 'zarrouk medium', '25', '4603', 'Lighting ');

-- --------------------------------------------------------

--
-- Table structure for table `bacteria`
--

CREATE TABLE `bacteria` (
  `id` int(10) NOT NULL,
  `name` varchar(300) DEFAULT NULL,
  `agar` varchar(300) DEFAULT NULL,
  `temperature` varchar(100) DEFAULT NULL,
  `storage` varchar(100) DEFAULT NULL,
  `remarks` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bacteria`
--

INSERT INTO `bacteria` (`id`, `name`, `agar`, `temperature`, `storage`, `remarks`) VALUES
(1, 'Lactobacillus casei', 'nutrient agar', '30°c', '4603', '');

-- --------------------------------------------------------

--
-- Table structure for table `biology_equipment`
--

CREATE TABLE `biology_equipment` (
  `id` int(10) NOT NULL,
  `name` varchar(300) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `link` varchar(2100) DEFAULT NULL,
  `unit_price` varchar(100) DEFAULT NULL,
  `location` varchar(300) DEFAULT NULL,
  `room` varchar(100) DEFAULT NULL,
  `date_purchased` varchar(100) DEFAULT NULL,
  `local_company` varchar(300) DEFAULT NULL,
  `check_po` varchar(300) DEFAULT NULL,
  `notes` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `biology_equipment`
--

INSERT INTO `biology_equipment` (`id`, `name`, `quantity`, `link`, `unit_price`, `location`, `room`, `date_purchased`, `local_company`, `check_po`, `notes`) VALUES
(1, 'Accu-Check Performa(Blood glucose meter)Expire30/11/2014', '1', '', '', '5C1', '', '', '', '', ''),
(2, 'Browguard and visor ', '2', '', '5.26', '', '4603', '', 'Scichem', 'OP/1997489', ''),
(3, 'Control test paper ', '10', 'ZGN040040', '127.7', '', '', '8/7/2013', 'Scichem', '', ''),
(4, 'Dialysis tubing  1*100 ft', '2', '', '1716', '', '4603', '8/11/2011', 'Phillipharris /APD Singapore PTE LTD', '4171', '');

-- --------------------------------------------------------

--
-- Table structure for table `chemical_stocklist`
--

CREATE TABLE `chemical_stocklist` (
  `id` int(10) NOT NULL,
  `name` varchar(300) DEFAULT NULL,
  `alternative_names` varchar(300) DEFAULT NULL,
  `prefix` varchar(300) DEFAULT NULL,
  `hazcard` varchar(300) DEFAULT NULL,
  `storage_group` varchar(300) DEFAULT NULL,
  `location` varchar(300) DEFAULT NULL,
  `quantity` varchar(300) DEFAULT NULL,
  `use_in_school` varchar(300) DEFAULT NULL,
  `comments` varchar(300) DEFAULT NULL,
  `shelf_life` varchar(300) DEFAULT NULL,
  `notes_for_check` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `chemical_stocklist`
--

INSERT INTO `chemical_stocklist` (`id`, `name`, `alternative_names`, `prefix`, `hazcard`, `storage_group`, `location`, `quantity`, `use_in_school`, `comments`, `shelf_life`, `notes_for_check`) VALUES
(1, 'sodium carbonate-10-water', 'sodium carbonate decanhydrte', '', '95A', 'GIn', '2/2', '1kg', 'All sec years', '', 'check', ''),
(2, 'sodium chloride', 'halite, rock salt', '', '47B', 'GIn', '2/2', '500g*4, 250g, 1kg*6', 'All sec years', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `chemistry_equipment`
--

CREATE TABLE `chemistry_equipment` (
  `id` int(10) NOT NULL,
  `name` varchar(300) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `order_number` varchar(300) DEFAULT NULL,
  `unit_price` varchar(100) DEFAULT NULL,
  `room` varchar(100) DEFAULT NULL,
  `date_purchased` varchar(100) DEFAULT NULL,
  `company` varchar(300) DEFAULT NULL,
  `notes` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `chemistry_equipment`
--

INSERT INTO `chemistry_equipment` (`id`, `name`, `quantity`, `order_number`, `unit_price`, `room`, `date_purchased`, `company`, `notes`) VALUES
(1, 'Adapter cone sc thread 13 B14/23', '6', '', '25.96', '4605', '7/17/2012', 'scichem', ''),
(2, 'White tile C00542', '32', '', '80.00', '4603', '8/7/2013', 'intereducation', '');

-- --------------------------------------------------------

--
-- Table structure for table `enzymes`
--

CREATE TABLE `enzymes` (
  `id` int(10) NOT NULL,
  `name` varchar(300) DEFAULT NULL,
  `description` varchar(300) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `package_quantity` varchar(100) DEFAULT NULL,
  `date_arrived` varchar(100) DEFAULT NULL,
  `expiry_date` varchar(100) DEFAULT NULL,
  `cat_number` varchar(300) DEFAULT NULL,
  `batch_number` varchar(300) DEFAULT NULL,
  `location` varchar(300) DEFAULT NULL,
  `remarks` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `enzymes`
--

INSERT INTO `enzymes` (`id`, `name`, `description`, `quantity`, `package_quantity`, `date_arrived`, `expiry_date`, `cat_number`, `batch_number`, `location`, `remarks`) VALUES
(1, 'a-Amylase', 'Bact.source', '17', '25GM', '11/10/2013', '3/6/2018', 'AM165', '188345/07', 'Glass room', ''),
(2, 'Bacterial alpha Amylase', 'contains reducing sugars', '1', '50g', '2009', '', 'F55385', 'K254', 'Chemical stroe room', ''),
(3, 'Catalase', 'Fungal enzyme', '5', '50ml', '2013', '', 'L12051', 'k993', 'Chemical stroe room', ''),
(4, 'Cellulase', '', '1', '2g', '4/8/2016', '', 'A01776', 'A257', 'Chemical stroe room', 'Use at pH 5.0 and at approx.25°C for optimum activity'),
(5, 'Diastase', '', '1', '100ml', '2000', '', 'H064305', 'O476', 'Glass room', 'Use at pH 3.5 to 5.0 (optimum = 4.0) Use at 20 to 60°C (optimum = 50°C)'),
(6, 'Fungal Amylase Powder', 'contains reducing sugars', '3', '50g', '2010', '', 'A01727', 'K507', 'Chemical stroe room', 'Use at pH 3.0 to 6.0 (optimum = 4.0) Use at 20 to 60°C (optimum =45°C)'),
(7, 'Invertase Concentrate', '', '1', '100ml', '', '', 'H064408', '013G', 'Chemical stroe room', 'Use at pH 4.0 to 6.5 (optimum = 4.5) Use at 40 to 65°C (optimum = 50°C)'),
(8, 'Lactase', 'B galactosidase', '1', '25ml', '2010', '', 'A01829', 'K538', 'Chemical stroe room', ''),
(9, 'Lipase', 'From pig pancreas', '4', '25g', '5/4/2016', '', '124741', '8968/7F', 'Chemical stroe room', 'Use at pH 6.0 to 9.0 (optimum = 7.5) Use at 20 to 50°C (optimum = 35°C)'),
(10, 'Lipase Powder', '', '6', '', '4/8/2016', '', 'A01831', 'A385', 'Chemical stroe room', ''),
(11, 'Lipase', 'Activity : 100,000 U/g', '1', '', '', '', '9004-34-6', '20160118-1', 'Chemical stroe room', 'Self life 12 months under 25 C'),
(12, 'Lysozyme hydrochlonide', '', '1', '25g', '', '', '', '', 'Chemical stroe room', ''),
(13, 'Pectinase Solution', '', '1', '100ml', '5/4/2016', '', 'A01867', 'A315', 'Chemical stroe room', 'Use at pH 2.0 to 9.0 (optimum = 7.0) Use at 20 to 75°C (optimum = 60°C)'),
(14, 'Pectinase Powder ', 'Activity : 10,000-30,000 U/g', '2', '100g', '', '', '9032-75-1', '20160710', 'Chemical stroe room', 'Self life 12 months under 25 C'),
(15, 'Pepsin Powder', '', '1', '', '', '', 'A01879', 'K342', 'Chemical stroe room', 'Use at pH 2.0 to 4.5 (optimum = 3.5) Use at 30 to 70°C (optimum = 60°C)'),
(16, 'Rennin Powder', '', '1', '5g', '11/19/2010', '', 'A01946', 'G562', 'Chemical stroe room', 'Use at pH 5.5 to 6.5 (optimum = 6.0) Use at 25 to 55°C (optimum = 40°C)'),
(17, 'Rennin Powder (Calf Stomach)', '', '6', '', '1/8/2017', '', 'A01958', 'A508', 'Glass room', ''),
(18, 'Trypsin Powder', 'from hog pancreas', '1', '50g', '11/19/2010', '', '', '', 'Chemical stroe room', 'Use at pH 5.0 to 10.5 (optimum = 7.5) Use at 20 to 65°C (optimum = 45°C)'),
(19, 'Urease Active Meal', 'Crude Urease', '2', '25g', '2009', '', 'F55897', 'K165', 'Chemical stroe room', 'Use at pH 6.0 to 9.0 (optimum = 7.0) Use at 20 to 70°C (optimum =65°C)');

-- --------------------------------------------------------

--
-- Table structure for table `glassware`
--

CREATE TABLE `glassware` (
  `id` int(10) NOT NULL,
  `name` varchar(300) DEFAULT NULL,
  `size` varchar(300) DEFAULT NULL,
  `quantity_4601` varchar(100) DEFAULT NULL,
  `quantity_4604` varchar(100) DEFAULT NULL,
  `quantity_4605` varchar(100) DEFAULT NULL,
  `quantity_4606` varchar(100) DEFAULT NULL,
  `quantity_4607` varchar(100) DEFAULT NULL,
  `quantity_4608` varchar(100) DEFAULT NULL,
  `quantity_4610` varchar(100) DEFAULT NULL,
  `quantity_4501` varchar(100) DEFAULT NULL,
  `quantity_4505` varchar(100) DEFAULT NULL,
  `minimum_for_year` varchar(300) DEFAULT NULL,
  `units` varchar(300) DEFAULT NULL,
  `number_in_stock` varchar(300) DEFAULT NULL,
  `order_required` varchar(300) DEFAULT NULL,
  `order_from` varchar(300) DEFAULT NULL,
  `code` varchar(300) DEFAULT NULL,
  `notes` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `glassware`
--

INSERT INTO `glassware` (`id`, `name`, `size`, `quantity_4601`, `quantity_4604`, `quantity_4605`, `quantity_4606`, `quantity_4607`, `quantity_4608`, `quantity_4610`, `quantity_4501`, `quantity_4505`, `minimum_for_year`, `units`, `number_in_stock`, `order_required`, `order_from`, `code`, `notes`) VALUES
(1, 'Beaker, Pyrex', '50ml', '43', '22', '38', '23', '35', '#', '30', '44', '24', '', '', '', 'Order Required', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `miscellaneous`
--

CREATE TABLE `miscellaneous` (
  `id` int(10) NOT NULL,
  `name` varchar(300) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `unit_price` varchar(100) DEFAULT NULL,
  `room` varchar(100) DEFAULT NULL,
  `date_purchased` varchar(100) DEFAULT NULL,
  `company` varchar(300) DEFAULT NULL,
  `check_po` varchar(300) DEFAULT NULL,
  `notes` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `miscellaneous`
--

INSERT INTO `miscellaneous` (`id`, `name`, `quantity`, `unit_price`, `room`, `date_purchased`, `company`, `check_po`, `notes`) VALUES
(1, 'Ruler wood -mark CM and MM pack of 10', '3', '1322.5', 'every room', '7/29/2011', 'Phillipharris /APD Singapore PTE LTD', 'P.O3938/PR3474/4017', ''),
(2, 'Basket ball size 3', '8', '350.0', '4603', '7/31/2012', '', '', ''),
(3, 'Batteries Panasonic AAA', '48', '17.5', '4603', '12/12/2012', '', '', ''),
(4, 'Cork line universal clamp ', '30', '107.0', '4603', '', '', 'PO6908&6878', '');

-- --------------------------------------------------------

--
-- Table structure for table `physics_equipment`
--

CREATE TABLE `physics_equipment` (
  `id` int(10) NOT NULL,
  `name` varchar(300) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `link` varchar(2100) DEFAULT NULL,
  `order_number` varchar(300) DEFAULT NULL,
  `unit_price` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `date_of_purchase` varchar(100) DEFAULT NULL,
  `purchased_from` varchar(300) DEFAULT NULL,
  `uses` varchar(300) DEFAULT NULL,
  `serial_number` varchar(300) DEFAULT NULL,
  `notes` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `physics_equipment`
--

INSERT INTO `physics_equipment` (`id`, `name`, `quantity`, `link`, `order_number`, `unit_price`, `location`, `date_of_purchase`, `purchased_from`, `uses`, `serial_number`, `notes`) VALUES
(1, 'Ammeter,black,3 scale,5A,50mA,500mA', '16', '', 'EMA0500010', '1242.25', '4603', '8/7/2013', 'scichem', '', '', ''),
(2, 'Conductivity paper', '5 set ', 'http://www.edulab.com/prod/conductive-paper-pk-10', '1440112-555', '719.48', '4603', '', 'Frey', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `posters`
--

CREATE TABLE `posters` (
  `id` int(10) NOT NULL,
  `name` varchar(300) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `code` varchar(300) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `company` varchar(300) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `posters`
--

INSERT INTO `posters` (`id`, `name`, `quantity`, `code`, `price`, `company`, `date`) VALUES
(1, 'Botany (Type of plant)', '1', 'PTE011', '1850.00', 'Intereducation', '7/31/2013'),
(2, 'Basic of Physic', '1', 'PTE051', '2100.00', 'Intereducation', '7/31/2013'),
(3, 'Physic II Optic', '1', 'PTE052', '1650.00', 'Intereducation', '7/31/2013'),
(4, 'General Science Microbiology', '1', 'PTE081', '1250.00', 'Intereducation', '7/31/2013'),
(5, 'General ScienceIV Ecosystems', '1', 'PTE084', '1850.00', 'Intereducation', '7/31/2013'),
(6, 'Physic unit poster', '5', 'XCA020010', '198.76', 'sci-chem', '8/7/2013'),
(7, 'Electromagnetic spectrum', '6', 'XPP03001', '1041.01', 'sci-chem', '8/7/2013'),
(8, 'Apparatus postersci chem', '5', 'XCP040020', '198.76', 'sci-chem', '8/7/2013'),
(9, 'Circuit symbol', '5', 'XEL670010', '198.76', 'sci-chem', '8/7/2013'),
(10, 'Food pyramid', '5', 'ZAC350030', '198.76', 'sci-chem', '8/7/2013');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(10) NOT NULL,
  `role` varchar(100) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `role`, `username`, `password`) VALUES
(1, 'Admin', 'admin1', 'Admin123'),
(2, 'Teacher', 'teacher1', 'Teacher123'),
(3, 'Student', 'student1', 'Student123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `algae`
--
ALTER TABLE `algae`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bacteria`
--
ALTER TABLE `bacteria`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `biology_equipment`
--
ALTER TABLE `biology_equipment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chemical_stocklist`
--
ALTER TABLE `chemical_stocklist`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chemistry_equipment`
--
ALTER TABLE `chemistry_equipment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `enzymes`
--
ALTER TABLE `enzymes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `glassware`
--
ALTER TABLE `glassware`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `miscellaneous`
--
ALTER TABLE `miscellaneous`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `physics_equipment`
--
ALTER TABLE `physics_equipment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `posters`
--
ALTER TABLE `posters`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `algae`
--
ALTER TABLE `algae`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `bacteria`
--
ALTER TABLE `bacteria`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `biology_equipment`
--
ALTER TABLE `biology_equipment`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `chemical_stocklist`
--
ALTER TABLE `chemical_stocklist`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `chemistry_equipment`
--
ALTER TABLE `chemistry_equipment`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `enzymes`
--
ALTER TABLE `enzymes`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT for table `glassware`
--
ALTER TABLE `glassware`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `miscellaneous`
--
ALTER TABLE `miscellaneous`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `physics_equipment`
--
ALTER TABLE `physics_equipment`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `posters`
--
ALTER TABLE `posters`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
