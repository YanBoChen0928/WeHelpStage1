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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'newtest','test','test',1,'2024-05-03 09:25:15'),(2,'Yanbo','ybchen','1',5,'2024-05-03 09:29:27'),(3,'A','a','2',10,'2024-05-03 09:29:27'),(4,'B','b','3',8,'2024-05-03 09:29:27'),(5,'C','c','4',7,'2024-05-03 09:29:27'),(6,'wehelpRenew2','wehelp','wehelp',0,'2024-05-11 10:13:01'),(7,'wehelp2','wehelp2','wehelp2',0,'2024-05-11 10:15:04'),(8,'wehelp3','wehelp3','wehelp3',0,'2024-05-11 10:40:08'),(9,'wehelp4','wehelp4','wehelp4',0,'2024-05-11 11:34:33'),(10,'wehelp5','wehelp5','wehelp5',0,'2024-05-11 12:02:29'),(11,'wehelp6','wehelp6','wehelp6',0,'2024-05-11 12:08:16'),(12,'我是wehelp7','wehelp7','wehelp7',0,'2024-05-11 20:52:15'),(13,'wehelp8','wehelp8','wehelp8',0,'2024-05-11 22:32:32'),(14,'G','111111','111111',0,'2024-05-11 22:38:12'),(15,'Simba','Simbauser','Simbapassword',0,'2024-05-12 14:30:41'),(16,'new people','new','new',0,'2024-05-12 15:29:45'),(17,'newpeople','new1','new1',0,'2024-05-12 15:54:10'),(18,'wehelp10','wehelp10','wehelp10',0,'2024-05-12 22:30:49'),(19,'陳彥伯','yanbo','yanbo',0,'2024-05-12 23:21:58'),(20,'劉怡君','zxc','zxc',0,'2024-05-15 22:35:45');
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
  `like_count` int(11) DEFAULT '0',
  `follower_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT 'Like Count',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Publish Time',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,1,'You are Good!',3,0,'2024-05-03 16:27:14'),(2,2,'I don\'t have the same opinion.',2,0,'2024-05-03 16:27:45'),(3,3,'lol lol lol lol lol',12,0,'2024-05-03 16:27:53'),(4,4,'pretty nice author and insightful words',15,0,'2024-05-03 16:28:03'),(5,5,'...',1,0,'2024-05-03 16:28:11'),(6,4,'excellent recommendation',10,0,'2024-05-03 17:23:02'),(7,3,'I like it!!!',0,0,'2024-05-12 11:38:57'),(8,13,'testtest',0,0,'2024-05-12 14:19:29'),(9,8,'TT~~~~',0,0,'2024-05-12 15:08:57'),(10,8,'strange',0,0,'2024-05-12 15:09:09'),(11,7,'modify {name} showing up after send new message',0,0,'2024-05-12 15:25:38'),(12,7,'weird, weird, weird, ',0,0,'2024-05-12 15:26:33'),(13,7,'continued~~',0,0,'2024-05-12 15:31:51'),(14,7,'多寫一些',0,0,'2024-05-12 15:33:46'),(15,7,'好像修好了？？？？？bug',0,0,'2024-05-12 15:34:02'),(16,10,'換我來進行',0,0,'2024-05-12 15:34:21'),(17,10,'這樣也可以～那用帳號登入',0,0,'2024-05-12 15:34:43'),(18,11,'wehelp6 進行測試',0,0,'2024-05-12 15:52:51'),(19,11,'wehelp6 沒有問題，那下面新註冊',0,0,'2024-05-12 15:53:07'),(20,18,'testtesttest',0,0,'2024-05-12 22:36:52'),(21,19,'5/12 23:00完成',0,0,'2024-05-12 23:22:12'),(22,6,'testtest 新功能上線',0,0,'2024-05-15 16:53:12'),(23,1,'測試',0,0,'2024-05-15 22:22:29'),(24,1,'5/15 22:20 完成 week7 的 task2',0,0,'2024-05-15 22:22:54'),(25,20,'我們家柴柴Simba好可愛喔！！！！',0,0,'2024-05-15 22:36:17'),(26,19,'對呀～聽說大家都說她萌萌達',0,0,'2024-05-15 22:37:38'),(27,1,'測試更新會員名字系統',0,0,'2024-05-18 07:29:45'),(28,12,'2024.5.18 更新姓名成功',0,0,'2024-05-18 08:13:33');
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

-- Dump completed on 2024-05-18 10:13:20
