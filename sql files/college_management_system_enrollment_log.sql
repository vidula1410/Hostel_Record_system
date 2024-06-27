CREATE DATABASE  IF NOT EXISTS `college_management_system` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `college_management_system`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: college_management_system
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `enrollment_log`
--

DROP TABLE IF EXISTS `enrollment_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enrollment_log` (
  `Log_ID` int NOT NULL AUTO_INCREMENT,
  `Student_ID` int DEFAULT NULL,
  `Enrollment_Date` timestamp NULL DEFAULT NULL,
  `Log_Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Log_ID`),
  KEY `Student_ID` (`Student_ID`),
  CONSTRAINT `enrollment_log_ibfk_1` FOREIGN KEY (`Student_ID`) REFERENCES `student` (`Student_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enrollment_log`
--

LOCK TABLES `enrollment_log` WRITE;
/*!40000 ALTER TABLE `enrollment_log` DISABLE KEYS */;
INSERT INTO `enrollment_log` VALUES (3,3,'2023-11-23 20:59:31','Ayush  enrolled in a mess.'),(4,4,'2023-11-23 21:04:57','Bhaskar KR enrolled in a mess.'),(5,5,'2023-11-23 21:05:01','Ashwin Sridhar enrolled in a mess.'),(6,6,'2023-11-23 21:05:07','Balaji M enrolled in a mess.'),(7,3,'2023-11-24 03:19:48','Ayush  enrolled in a mess.'),(8,3,'2023-11-24 03:34:24','Ayush  enrolled in a mess.'),(9,5,'2023-11-24 03:41:04','Ashwin Sridhar enrolled in a mess.'),(10,5,'2023-11-24 03:45:41','Ashwin Sridhar enrolled in a mess.'),(11,5,'2023-11-24 03:45:58','Ashwin Sridhar enrolled in a mess.'),(12,7,'2023-11-24 04:45:20','Balaji  Rock  enrolled in a mess.');
/*!40000 ALTER TABLE `enrollment_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-24 11:16:07
