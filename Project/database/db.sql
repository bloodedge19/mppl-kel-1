-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: imployee
-- ------------------------------------------------------
-- Server version	8.0.31-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `email` char(50) NOT NULL,
  `address` char(50) DEFAULT NULL,
  `phone_number` char(50) DEFAULT NULL,
  `password` char(60) DEFAULT NULL,
  `fullname` char(50) NOT NULL,
  `salary` int NOT NULL,
  `overtime_salary` int DEFAULT NULL,
  `isHR` tinyint(1) NOT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1235 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'admin@imployee.id',NULL,NULL,'$2b$12$rB5nHIT2K98lgtNPNf/qGOPFyKqIuDZ.BE5KhWRqc13un6Iq5125C','Alvina Maharni',12000000,120000,1),(3,'asd@gmail.com',NULL,NULL,'$2b$12$eEH/5m1cav..1Rlin9rDeO0LMCciqLB5tND73SzuX4sVZC2FjjEBS','asd',123,NULL,0),(4,'testing@gmail.com',NULL,NULL,'$2b$12$rB5nHIT2K98lgtNPNf/qGOPFyKqIuDZ.BE5KhWRqc13un6Iq5125C','testing',12000000,120000,0),(123,'haha@gmail.com','test','test','$2b$12$B5XIy23a0JRYkAVY8NvnDe5hNNSv4LY.25RgmunbarQwN09LWGZCe','Test',11,NULL,0),(1234,'haha2@gmail.com','test','test','$2b$12$KC.aLUAgBtaNEskkWHR/s.3kRESAL0Lm1C1qSqYqTGE/Nnx3uQ9Ee','Test',11,NULL,0);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_employees`
--

DROP TABLE IF EXISTS `log_employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log_employees` (
  `log_id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int DEFAULT NULL,
  `clock_in` datetime DEFAULT NULL,
  `clock_out` datetime DEFAULT NULL,
  `permit` datetime DEFAULT NULL,
  `working_hours` time DEFAULT NULL,
  PRIMARY KEY (`log_id`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `log_employees_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log_employees`
--

LOCK TABLES `log_employees` WRITE;
/*!40000 ALTER TABLE `log_employees` DISABLE KEYS */;
INSERT INTO `log_employees` VALUES (3,4,'2022-11-25 17:34:27','2022-11-25 19:34:27',NULL,'02:00:00'),(8,1,'2022-11-27 22:09:10','2022-11-27 23:08:37',NULL,'00:59:27'),(9,4,'2022-11-27 23:10:59','2022-11-27 23:19:51',NULL,'00:08:52'),(11,4,'2022-11-28 22:02:34','2022-11-28 22:03:13',NULL,'00:00:39'),(12,4,'2022-11-29 20:58:20','2022-11-29 20:58:58',NULL,'00:00:38'),(13,4,'2022-11-30 14:41:04','2022-11-30 14:41:15',NULL,'00:00:11'),(14,3,'2022-11-30 15:00:05','2022-11-30 15:00:15',NULL,'00:00:10'),(15,4,'2022-12-01 07:13:05',NULL,NULL,NULL);
/*!40000 ALTER TABLE `log_employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payroll`
--

DROP TABLE IF EXISTS `payroll`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payroll` (
  `payroll_id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`payroll_id`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `payroll_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payroll`
--

LOCK TABLES `payroll` WRITE;
/*!40000 ALTER TABLE `payroll` DISABLE KEYS */;
INSERT INTO `payroll` VALUES (1,4,0);
/*!40000 ALTER TABLE `payroll` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reimbursement`
--

DROP TABLE IF EXISTS `reimbursement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reimbursement` (
  `reimbursement_id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int DEFAULT NULL,
  `type` char(32) NOT NULL,
  `date` datetime NOT NULL,
  `amount` int NOT NULL,
  `description` text NOT NULL,
  `status` enum('Waiting','Approved','Rejected') NOT NULL,
  PRIMARY KEY (`reimbursement_id`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `reimbursement_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reimbursement`
--

LOCK TABLES `reimbursement` WRITE;
/*!40000 ALTER TABLE `reimbursement` DISABLE KEYS */;
INSERT INTO `reimbursement` VALUES (1,4,'Mobile Bills','2022-12-01 00:00:00',123,'123','Waiting'),(2,4,'Mobile Bills','2022-12-01 07:09:10',123,'123','Waiting');
/*!40000 ALTER TABLE `reimbursement` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-01  7:15:01
