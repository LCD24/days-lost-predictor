-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: days_off_database
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `acidente`
--

DROP TABLE IF EXISTS `acidente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `acidente` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_funcionario` int NOT NULL,
  `id_area_trabalho` int NOT NULL,
  `id_zona_corpo_atingida` int NOT NULL,
  `id_tipo_lesao` int NOT NULL,
  `dias_perdidos` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_funcionario` (`id_funcionario`),
  KEY `id_area_trabalho` (`id_area_trabalho`),
  KEY `id_zona_corpo_atingida` (`id_zona_corpo_atingida`),
  KEY `id_tipo_lesao` (`id_tipo_lesao`),
  CONSTRAINT `acidente_ibfk_1` FOREIGN KEY (`id_funcionario`) REFERENCES `funcionario` (`id`),
  CONSTRAINT `acidente_ibfk_2` FOREIGN KEY (`id_area_trabalho`) REFERENCES `area_trabalho` (`id_area_trabalho`),
  CONSTRAINT `acidente_ibfk_3` FOREIGN KEY (`id_zona_corpo_atingida`) REFERENCES `zona_corpo_atingida` (`id_zona_corpo_atingida`),
  CONSTRAINT `acidente_ibfk_4` FOREIGN KEY (`id_tipo_lesao`) REFERENCES `tipo_lesao` (`id_tipo_lesao`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acidente`
--

LOCK TABLES `acidente` WRITE;
/*!40000 ALTER TABLE `acidente` DISABLE KEYS */;
/*!40000 ALTER TABLE `acidente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `area_trabalho`
--

DROP TABLE IF EXISTS `area_trabalho`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `area_trabalho` (
  `id_area_trabalho` int NOT NULL AUTO_INCREMENT,
  `area_trabalho` varchar(255) NOT NULL,
  PRIMARY KEY (`id_area_trabalho`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `area_trabalho`
--

LOCK TABLES `area_trabalho` WRITE;
/*!40000 ALTER TABLE `area_trabalho` DISABLE KEYS */;
/*!40000 ALTER TABLE `area_trabalho` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcao`
--

DROP TABLE IF EXISTS `funcao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcao` (
  `id_funcao` int NOT NULL AUTO_INCREMENT,
  `funcao` varchar(255) NOT NULL,
  PRIMARY KEY (`id_funcao`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `funcionario`
--

DROP TABLE IF EXISTS `funcionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idade_funcionario` int NOT NULL,
  `id_funcao` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_funcao` (`id_funcao`),
  CONSTRAINT `funcionario_ibfk_1` FOREIGN KEY (`id_funcao`) REFERENCES `funcao` (`id_funcao`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionario`
--

LOCK TABLES `funcionario` WRITE;
/*!40000 ALTER TABLE `funcionario` DISABLE KEYS */;
/*!40000 ALTER TABLE `funcionario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_lesao`
--

DROP TABLE IF EXISTS `tipo_lesao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_lesao` (
  `id_tipo_lesao` int NOT NULL AUTO_INCREMENT,
  `tipo_lesao` varchar(255) NOT NULL,
  PRIMARY KEY (`id_tipo_lesao`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_lesao`
--

LOCK TABLES `tipo_lesao` WRITE;
/*!40000 ALTER TABLE `tipo_lesao` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_lesao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zona_corpo_atingida`
--

DROP TABLE IF EXISTS `zona_corpo_atingida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zona_corpo_atingida` (
  `id_zona_corpo_atingida` int NOT NULL AUTO_INCREMENT,
  `zona_corpo_atingida` varchar(255) NOT NULL,
  PRIMARY KEY (`id_zona_corpo_atingida`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zona_corpo_atingida`
--

LOCK TABLES `zona_corpo_atingida` WRITE;
/*!40000 ALTER TABLE `zona_corpo_atingida` DISABLE KEYS */;
/*!40000 ALTER TABLE `zona_corpo_atingida` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-23 14:47:26
