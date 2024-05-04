-- MySQL dump 10.13  Distrib 8.0.18, for macos10.14 (x86_64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.0.18

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
-- Table structure for table `joint_table`
--

DROP TABLE IF EXISTS `joint_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `joint_table` (
  `id` bigint(20) NOT NULL DEFAULT '0' COMMENT 'Unique ID',
  `member_id` bigint(20) NOT NULL COMMENT 'Member ID for Message Sender',
  `content` varchar(255) NOT NULL COMMENT 'Content',
  `like_count` int(10) unsigned NOT NULL COMMENT 'Password',
  `follower_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT 'Like Count',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Publish Time',
  `username` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `joint_table`
--

LOCK TABLES `joint_table` WRITE;
/*!40000 ALTER TABLE `joint_table` DISABLE KEYS */;
INSERT INTO `joint_table` VALUES (1,1,'You are Good!',3,0,'2024-05-03 16:27:14','test'),(2,2,'I don\'t have the same opinion.',2,0,'2024-05-03 16:27:45','ybchen'),(3,3,'lol lol lol lol lol',12,0,'2024-05-03 16:27:53','a'),(4,4,'pretty nice author and insightful words',15,0,'2024-05-03 16:28:03','b'),(5,5,'...',1,0,'2024-05-03 16:28:11','c');
/*!40000 ALTER TABLE `joint_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID',
  `name` varchar(255) NOT NULL COMMENT 'Name',
  `username` varchar(255) NOT NULL COMMENT 'Username',
  `password` varchar(255) NOT NULL COMMENT 'Password',
  `follower_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT 'Follower Count',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'test2','test','test',1,'2024-05-03 09:25:15'),(2,'Yanbo','ybchen','1',5,'2024-05-03 09:29:27'),(3,'A','a','2',10,'2024-05-03 09:29:27'),(4,'B','b','3',8,'2024-05-03 09:29:27'),(5,'C','c','4',7,'2024-05-03 09:29:27');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID',
  `member_id` bigint(20) NOT NULL COMMENT 'Member ID for Message Sender',
  `content` varchar(255) NOT NULL COMMENT 'Content',
  `like_count` int(10) unsigned NOT NULL COMMENT 'Password',
  `follower_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT 'Like Count',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Publish Time',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,1,'You are Good!',3,0,'2024-05-03 16:27:14'),(2,2,'I don\'t have the same opinion.',2,0,'2024-05-03 16:27:45'),(3,3,'lol lol lol lol lol',12,0,'2024-05-03 16:27:53'),(4,4,'pretty nice author and insightful words',15,0,'2024-05-03 16:28:03'),(5,5,'...',1,0,'2024-05-03 16:28:11'),(6,4,'excellent recommendation',10,0,'2024-05-03 17:23:02');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_member`
--

DROP TABLE IF EXISTS `test_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_member` (
  `Column_Name` varchar(255) NOT NULL,
  `Data_Type` varchar(255) NOT NULL,
  `Additional_Settings` varchar(255) DEFAULT NULL,
  `Description` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_member`
--

LOCK TABLES `test_member` WRITE;
/*!40000 ALTER TABLE `test_member` DISABLE KEYS */;
INSERT INTO `test_member` VALUES ('id','bigint','primary key auto_increment','Unique ID'),('name','varchar(255)','not null','Name'),('username','varchar(255)','not null','Username'),('password','varchar(255)','not null','Password'),('follower_count','int unsigned','not null, default to 0','Follower Count'),('time','datetime','not null, default to current time','Signup Time');
/*!40000 ALTER TABLE `test_member` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-04  6:31:03
