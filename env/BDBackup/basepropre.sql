-- MySQL dump 10.13  Distrib 5.5.40, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mouvinsa
-- ------------------------------------------------------
-- Server version	5.5.40-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `badge`
--

DROP TABLE IF EXISTS `badge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `badge` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `label` varchar(127) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `badge`
--

LOCK TABLES `badge` WRITE;
/*!40000 ALTER TABLE `badge` DISABLE KEYS */;
/*!40000 ALTER TABLE `badge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `badges_person`
--

DROP TABLE IF EXISTS `badges_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `badges_person` (
  `person_id` int(11) DEFAULT NULL,
  `badge_id` int(11) DEFAULT NULL,
  KEY `person_id` (`person_id`),
  KEY `badge_id` (`badge_id`),
  CONSTRAINT `badges_person_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`),
  CONSTRAINT `badges_person_ibfk_2` FOREIGN KEY (`badge_id`) REFERENCES `badge` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `badges_person`
--

LOCK TABLES `badges_person` WRITE;
/*!40000 ALTER TABLE `badges_person` DISABLE KEYS */;
/*!40000 ALTER TABLE `badges_person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `city`
--

DROP TABLE IF EXISTS `city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `label` varchar(127) NOT NULL,
  `lattitude` float NOT NULL,
  `longitude` float NOT NULL,
  `caption` varchar(255) DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city`
--

LOCK TABLES `city` WRITE;
/*!40000 ALTER TABLE `city` DISABLE KEYS */;
/*!40000 ALTER TABLE `city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `city_goal`
--

DROP TABLE IF EXISTS `city_goal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `city_goal` (
  `city_id` int(11) DEFAULT NULL,
  `goal_id` int(11) DEFAULT NULL,
  KEY `city_id` (`city_id`),
  KEY `goal_id` (`goal_id`),
  CONSTRAINT `city_goal_ibfk_1` FOREIGN KEY (`city_id`) REFERENCES `city` (`id`),
  CONSTRAINT `city_goal_ibfk_2` FOREIGN KEY (`goal_id`) REFERENCES `goal` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city_goal`
--

LOCK TABLES `city_goal` WRITE;
/*!40000 ALTER TABLE `city_goal` DISABLE KEYS */;
/*!40000 ALTER TABLE `city_goal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `affiliation` varchar(255) DEFAULT NULL,
  `position` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`id`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (4,'DRI','Chargée de projets Européens'),(5,'DirFor & Humas',''),(6,'SCOLARITE','Secretaire Scolarité'),(15,'humas','secrétaire'),(16,'humas','secrétaire'),(17,'CDS','Secrétaire SSHN'),(18,'MATEIS','SECRETAIRE GESTIONNAIRE '),(19,'',''),(20,'',''),(21,'lamcos- Jean d\'Alembert','secrétaire de laboratoire'),(23,'',''),(24,'',''),(25,'Laboratorie MATEIS','Responsable de la plateforme TP matériaux'),(26,'SGM-MATEIS','Directeur du Département SGM'),(27,'',''),(28,'',''),(31,'',''),(32,'LIRIS','Enseignant/chercheur'),(33,'Insa/Insavalor','ATER'),(38,'DSI','Technicien informtique'),(45,'DSI','Personnel '),(46,'','Centre des humanités'),(47,'MATEIS/SGM','Maitre de conférence'),(52,'GEN','secrétaire'),(53,'Doc\'INSA','Bibliothécaire'),(55,'BMC','Documentaliste'),(56,'BMC','BIBLIOTH2CAIRE'),(57,'',''),(58,'','Responsable administratif (SEFDI)'),(59,'',''),(60,'Centre Diversité et Réussite','Chargée de programmes'),(61,'Bibliothèque Marie Curie','Documentaliste'),(62,'DRH','Responsable projets RH'),(63,'INL',''),(64,'Dirpat','Développement durable'),(66,'','secrétaire au centre des Humanités'),(67,'',''),(68,'DISP - GI','MCF Génie Industriel'),(69,'','Enseignante'),(72,'Bibliothèque Marie Curie','Bibliothécaire'),(74,'',''),(75,'','Assistante Direction DRE/FONDATION'),(76,'Biblilothèque Marie Curie','bibliothécaire'),(78,'Direction du Patrimoine','Chef du service de logistique'),(79,'Fondation INSA Lyon','Chargée de programmes'),(90,'Humanités','enseignant'),(92,'',''),(97,'',''),(99,'','Maître de conférences - Directeur des Etudes'),(102,'','enseignante'),(103,'',''),(104,'Labo LVA - Département PC','Enseignant-Chercheur'),(105,'DISP','MCF'),(106,'IF/LIRIS','MCF'),(107,'',''),(108,'GMC','Assitante  GMC filières apprentissage'),(109,'',''),(113,'Département IF / Laboratoire CITI / INSA de Lyon','Maître de conférences'),(114,'Bibliothèque Marie Curie','Bibliothécaire'),(117,'',''),(118,'','Bibliothécaire'),(119,'',''),(122,'','Professeur'),(123,'',''),(125,'Département Génie Electrique','Secrétaire département GE'),(130,'',''),(133,'',''),(134,'LaMCoS','Professeur'),(135,'',''),(136,'','Secrétaire DARED'),(139,'LIRIS','Maitre de Conférences'),(140,'BMC',''),(141,'SCD Doc INSA','Prof des universités/ documentaliste'),(142,'DRH','Gestionnaire RH'),(144,'Bibliothèque','Employée de bibliothèque'),(145,'','IGE (Cethil)'),(146,'???','Responsable des études de GMC'),(147,'','Directeur filière apprentissage'),(150,'','Secrétaire stages et RI départ. GCU'),(151,'','ensei'),(155,'',''),(156,'',''),(157,'',''),(163,'',''),(164,'',''),(165,'CNRS - LaMCoS','Chercheur'),(166,'','Directeur-Adjoint du PC'),(167,'',''),(169,'',''),(172,'',''),(180,'LIRIS','Enseignant-Chercheur'),(181,'',''),(182,'ICJ - INSA','Enseignant-Chercheur'),(183,'','Psychologue'),(184,'ICJ - INSA','Enseignant Chercheur'),(185,'','professeur d\'anglais'),(186,'DARED Insa Direction','Assistante administrative'),(187,'BS/MAP','Enseignant-chercheur'),(191,'DRE/Fondation','Technicien BDD'),(192,'DRH','Responsable Pole EC'),(196,'Pôle de mathématiques /  ICJ','MC mathematiques GE'),(197,'',''),(200,'','Responsable administrative DRI'),(202,'','PrAg Maths'),(203,'',''),(204,'Directions Relations Internationales','Chargée de projets Asie'),(206,'',''),(208,'','PRAG Maths'),(213,'DRI','Assistante de direction '),(214,'',''),(216,'',''),(218,'Centre des Humanités','enseignant Humas');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fitness_info`
--

DROP TABLE IF EXISTS `fitness_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fitness_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) DEFAULT NULL,
  `stepSum` int(11) DEFAULT NULL,
  `streak` int(11) DEFAULT NULL,
  `bestStreak` int(11) DEFAULT NULL,
  `goal` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `person_id` (`person_id`),
  CONSTRAINT `fitness_info_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fitness_info`
--

LOCK TABLES `fitness_info` WRITE;
/*!40000 ALTER TABLE `fitness_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `fitness_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goal`
--

DROP TABLE IF EXISTS `goal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `difficulty` enum('difficile','moyen','facile') NOT NULL,
  `label` varchar(45) NOT NULL,
  `distance` int(11) NOT NULL,
  `image` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goal`
--

LOCK TABLES `goal` WRITE;
/*!40000 ALTER TABLE `goal` DISABLE KEYS */;
/*!40000 ALTER TABLE `goal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group`
--

DROP TABLE IF EXISTS `group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `label` varchar(127) NOT NULL,
  `slogan` varchar(255) DEFAULT NULL,
  `stepSum` int(11) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `goal_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `goal_id` (`goal_id`),
  CONSTRAINT `group_ibfk_1` FOREIGN KEY (`goal_id`) REFERENCES `goal` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group`
--

LOCK TABLES `group` WRITE;
/*!40000 ALTER TABLE `group` DISABLE KEYS */;
INSERT INTO `group` VALUES (1,'Jumperzap',NULL,0,NULL,NULL),(2,'Highjumps',NULL,0,NULL,NULL),(3,'Batsqueak',NULL,0,NULL,NULL),(4,'Athletebrring',NULL,0,NULL,NULL),(5,'Sportouch',NULL,0,NULL,NULL),(6,'Catcherparp',NULL,0,NULL,NULL),(7,'Frisbeeplonk',NULL,0,NULL,NULL),(8,'Skateroar',NULL,0,NULL,NULL),(9,'Tiecheep',NULL,0,NULL,NULL),(10,'Tennisbuzz',NULL,0,NULL,NULL),(11,'Volleytweet',NULL,0,NULL,NULL),(12,'Gearmeow',NULL,0,NULL,NULL),(13,'Outslouch',NULL,0,NULL,NULL),(14,'Hockeytwang',NULL,0,NULL,NULL),(15,'Rowingthump',NULL,0,NULL,NULL),(16,'Uniformfizz',NULL,0,NULL,NULL),(17,'Walkgrowl',NULL,0,NULL,NULL),(18,'Hardballping',NULL,0,NULL,NULL),(19,'Freethrowrip',NULL,0,NULL,NULL),(20,'Golfingsmash',NULL,0,NULL,NULL),(21,'Championouch',NULL,0,NULL,NULL),(22,'Hockeyhoot',NULL,0,NULL,NULL),(23,'Lutzboink',NULL,0,NULL,NULL),(24,'Fitnesstweet',NULL,0,NULL,NULL),(25,'Bowlingbelch',NULL,0,NULL,NULL),(26,'Runningshush',NULL,0,NULL,NULL),(27,'Surferfizz',NULL,0,NULL,NULL),(28,'Batbeep',NULL,0,NULL,NULL),(29,'Biathlonboom',NULL,0,NULL,NULL),(30,'Battingbuzz',NULL,0,NULL,NULL),(31,'Cyclingcuckoo',NULL,0,NULL,NULL),(32,'Dartdingdong',NULL,0,NULL,NULL),(33,'Divedrip',NULL,0,NULL,NULL),(34,'Fitnessfizzle',NULL,0,NULL,NULL),(35,'Footballfizz',NULL,0,NULL,NULL),(36,'Boxingboom',NULL,0,NULL,NULL),(37,'Movementbuzz',NULL,0,NULL,NULL),(38,'Waterskiwoof',NULL,0,NULL,NULL),(39,'Canoeingcheep',NULL,0,NULL,NULL),(40,'Crazy Legs',NULL,0,NULL,NULL),(41,'Catchmurmer',NULL,0,NULL,NULL);
/*!40000 ALTER TABLE `group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `migrate_version`
--

DROP TABLE IF EXISTS `migrate_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `migrate_version` (
  `repository_id` varchar(250) NOT NULL,
  `repository_path` text,
  `version` int(11) DEFAULT NULL,
  PRIMARY KEY (`repository_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `migrate_version`
--

LOCK TABLES `migrate_version` WRITE;
/*!40000 ALTER TABLE `migrate_version` DISABLE KEYS */;
INSERT INTO `migrate_version` VALUES ('database repository','/app/mouvinsa/db_repository',4);
/*!40000 ALTER TABLE `migrate_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(120) NOT NULL,
  `password` varchar(120) NOT NULL,
  `nickname` varchar(120) NOT NULL,
  `sex` varchar(50) NOT NULL,
  `firstname` varchar(120) DEFAULT NULL,
  `lastname` varchar(120) DEFAULT NULL,
  `birthdate` datetime DEFAULT NULL,
  `weight` float DEFAULT NULL,
  `height` float DEFAULT NULL,
  `category` enum('etudiant','enseignant','iatos') NOT NULL,
  `type` varchar(50) DEFAULT NULL,
  `etat` enum('PREREGISTERED','REGISTERED','DROPPED') NOT NULL,
  `token` varchar(128) DEFAULT NULL,
  `image` varchar(120) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `nickname` (`nickname`),
  UNIQUE KEY `token` (`token`),
  KEY `group_id` (`group_id`),
  CONSTRAINT `person_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=220 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES (4,'thalia.darnanville@insa-lyon.fr','a4f7cfb62fd8d07b3b858d37323f4398b42dc5fb9f923e30af96cd461e2ddd12:e2ccae7efb284f709853a0bb8cf69c8f','Europas','Feminin','Thalia','Darnanville','1977-07-13 00:00:00',62,171,'iatos','employee','PREREGISTERED',NULL,'0',1),(5,'matthieu.royet@insa-lyon.fr','9ae29386f0c1da53a99e5470c041fb2ccfa5d610be456c9041fc6e441ce76420:e22666a395bc481db43887b6e7e23101','Matthieu','Masculin','Matthieu','Royet','1966-11-01 00:00:00',90,178,'iatos','employee','PREREGISTERED',NULL,'0',2),(6,'chantal.michel@insa-lyon.fr','4662ed983ec845e68cebdebb3e4db9755bcacc198c39f1b46715a5f64d0744d7:630a9d12aee64d9fa3971f18715f4263','chantoune','Feminin','Chantal','MICHEL','1962-01-25 00:00:00',54,157,'iatos','employee','PREREGISTERED',NULL,'0',3),(7,'quentin.lemaire@insa-lyon.fr','5f9fa9269d8c2c6f05a340c6fd216b5e84592cd623a281bb7113b39f470fe5de:4c1e3424bd99474f8cc25a20e0d2b61d','Quentin','Masculin','Quentin','Lemaire',NULL,NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',1),(8,'maria.etegan@insa-lyon.fr','adeee5cd4c371b189dd2c3ad3c7a90fdaf3c0ac4695687388801deb70a8b7bc6:51896d2734504c9d931e820ebd3c56f6','cosmina','Inconnu','','',NULL,NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',2),(10,'bernardo.rittmeyer@insa-lyon.fr','24ed7ee555cb8d7057bd08791863f8ada2fa79cab0aa921d2e173520162bef65:7e48ce30f151496e8620a841628064bd','rittme','Masculin','Rittmeyer','Bernardo','1988-12-13 00:00:00',68,182,'etudiant','student','PREREGISTERED',NULL,'0',3),(11,'vadim.caen@insa-lyon.fr','11cf53269b7c42672c30c46b38a4dbe5265440f4491dea691bb9d059f73400c0:d9d0c8375f39441cb4981bb72545e620','dimsum','Masculin','vadim','caen','1993-12-12 00:00:00',63,184,'etudiant','student','PREREGISTERED',NULL,'0',4),(13,'marco.montalto@insa-lyon.fr','5e1500416e62320e1bdf20526c7f745cbf4d7c1aba6771e0e274f3c44c6e12df:efab092647f64f0c83941adfb297eca7','marcuccissimo','Masculin','Marco','Montalto','1993-02-21 00:00:00',75,175,'etudiant','student','PREREGISTERED',NULL,'0',5),(14,'edouard.oger@insa-lyon.fr','74d2e3da35dcae517238a06ed937567c73251f57304acf21d86c9e5f3fddb352:bc0608b8da414fdcb0e6a94969413114','eog','Masculin','edouard','Oger','1990-10-15 00:00:00',90,188,'etudiant','student','PREREGISTERED',NULL,'0',6),(15,'marie.rousseau@insa-lyon.fr','0a436f830f28a5072c63876b50e6d01dc13a62441af2a1dde1380d5debf944aa:ffa2870ab8194e86aa35911282762ffb','marie','Feminin','Marie','ROUSSEAU','1966-07-22 00:00:00',69,170,'iatos','employee','PREREGISTERED',NULL,'0',4),(16,'carine.bruscella@insa-lyon.fr','8698745817d7e7efd8bc23bc1e1e666a2699f6eaf0fad2f9d6027a66ded15251:3588e02237ee46c9935273131d95e5d8','carine','Feminin','carine','bruscella','1969-06-20 00:00:00',62,160,'iatos','employee','PREREGISTERED',NULL,'0',5),(17,'beatrice.marchand@insa-lyon.fr','9bf7e267010c347be62967df24f93cb966d4d00c64f1f37cf9daa4d7a83df0c9:7bbfe463e1864e5ab6de9f23ae906510','bea','Feminin','Béatrice','MARCHAND','1972-04-18 00:00:00',67,168,'iatos','employee','PREREGISTERED',NULL,'0',6),(18,'corinne.payen@insa-lyon.fr','36b1d9ae8706fe576c4bc42be53a39967e4809c2126e8f908db6cf115c84f60f:4e42407149ae4ffb80841521929377ff','magritta','Feminin','CORINNE','PAYEN','1961-06-19 00:00:00',95,173,'iatos','employee','PREREGISTERED',NULL,'0',7),(19,'evelyne.parra@insa-lyon.fr','769158b5069fe214c15c7eca087ac5e36afbb81eb289e430fe426767440102a5:c2b745125be1459085daee38793ee31d','evel','Feminin','EVELYNE','PARRA','1957-09-01 00:00:00',45,157,'iatos','employee','PREREGISTERED',NULL,'0',8),(20,'francoise.leboutet@insa-lyon.fr','3621e9746e0d5dbcb2fd46eb0abe004e6d5206ef596209b7e55d02718d4767ab:554e17a5fc334c2db2fe2c7a7d8c5434','framboise','Feminin','françoise','LEBOUTET','1953-12-04 00:00:00',53,160,'iatos','employee','PREREGISTERED',NULL,'0',9),(21,'sophie.de-oliveira@insa-lyon.fr','71725ff08d43e94d9e493831226242c42dd3c784ae92d4cdc930b18ba2bd3bf7:7b4994ca6fdb4684b72a8bb7a1acd54f','sdeoliveir','Feminin','SOPHIE','De Oliveira','1981-04-25 00:00:00',57,171,'iatos','employee','PREREGISTERED',NULL,'0',10),(23,'nathalie.jarno@insa-lyon.fr','b687e95422aadf48ddfc254f5368227c0dd85155b229885c11570c63aa4da828:491dfff154fb4e63a76f340e93492078','Verlaine','Inconnu','','',NULL,NULL,NULL,'iatos','employee','PREREGISTERED',NULL,'0',11),(24,'renaud.rinaldi@insa-lyon.fr','cd534f31ea9074a89d5e4b73771b5f7e20b2856ca9244ea76ef3f293864e18a8:685acd77f12546678bc304590562b502','Rono','Inconnu','','',NULL,NULL,NULL,'enseignant','employee','PREREGISTERED',NULL,'0',1),(25,'christophe.le-bourlot@insa-lyon.fr','9bc711dec3fb57b45dcf65ec7327f3fcefc4f68d2b1eaef3631a825a5cfdb07b:4b9415c408984c1b9eb888ec88cf5cce','Xtof','Masculin','Le Bourlot','Christophe','1984-07-28 00:00:00',75,180,'enseignant','employee','PREREGISTERED',NULL,'0',2),(26,'xavier.kleber@insa-lyon.fr','08f12fe624b902b1d63158f1d5272919da34e8f469c0c7600892b51a0a8a8067:765bc5c76cc54495b572581ce910a365','Xavier_K','Masculin','xavier','kleber','1971-07-08 00:00:00',85,180,'enseignant','employee','PREREGISTERED',NULL,'0',3),(27,'zeina.hamam@insa-lyon.fr','089d9943f76373ea6e1d74b3200f988036760cc476602fe79c62083f82d0e03d:83e97377da444276a33b273bc597a415','Zeina','Feminin','HAMAM','Zeina','1984-04-08 00:00:00',53,155,'enseignant','employee','PREREGISTERED',NULL,'0',4),(28,'marie-christine.faye@insa-lyon.fr','fbb1764bebfc159cbb12eb2d6acb32b67b7f1a0d1b13634c81bfa5b99d7f7202:e696c66977154c19a72708a722037857','MC','Inconnu','','',NULL,NULL,NULL,'iatos','employee','PREREGISTERED',NULL,'0',12),(29,'ludmila.danilescu@insa-lyon.fr','e8ecf392109408eacab4f7ab0705ae23225559b1afea8e1789e4de707bc70fe7:b24c1e4efb9049e299ddbc9475110ef7','Neige','Feminin','Ludmila','Danilescu','1991-08-25 00:00:00',58,167,'etudiant','student','PREREGISTERED',NULL,'0',7),(30,'margaux.pourret@insa-lyon.fr','5bde6b0e70fe95d99813d22a9539e1bd993f7143ca471bb70f6a3525f9123564:34a1c28aa8c14237a281f6909b675d80','Mxp','Inconnu','','',NULL,NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',8),(31,'frida.tidadini@insa-lyon.fr','4780cb54e51828f3194274b0b7a8960214db038d1fbe569fb39650fbe633f01a:be26bf3703164d6e8583bdd2c50eeedf','fridoulle','Inconnu','','',NULL,NULL,NULL,'iatos','employee','PREREGISTERED',NULL,'0',13),(32,'youssef.amghar@insa-lyon.fr','acdd90a4568d12a08227f4ae23d07e48cce2da2e464c1cf67289dcdcf7206f39:69419355c1f64b6f821a981ae6030d29','youssef','Masculin','Youssef','Amghar','1956-07-06 00:00:00',82,180,'enseignant','employee','PREREGISTERED',NULL,'0',5),(33,'rim.guetari@insa-lyon.fr','1196f82fa4b72b556e3f213e686b7d650ff008eeb06b92e4147f0279756a60a6:259c6f5f7056461eaff9093f3a288192','rguetari','Feminin','rim','guetari','1987-01-24 00:00:00',65,169,'enseignant','employee','PREREGISTERED',NULL,'0',6),(34,'laurentiu.capatina@insa-lyon.fr','e850fbb896db68f62d75078e8e9631705ac8d2873a4721a86c67d51f54ec76a4:17364743bbcd4dc18d104e14dc2ca825','Lau','Masculin','Laurentiu','Capatina','1992-08-08 00:00:00',72,187,'etudiant','student','PREREGISTERED',NULL,'0',22),(35,'mathieu.thoretton@insa-lyon.fr','a4ffec6fa796580c81ac79a40a4561877fd14d43a916cc1d191e38ae1cf8692e:dd8b59b9f54349a7b3bff7d1a397fb98','mtho','Masculin','Mathieu','Thoretton','1993-06-01 00:00:00',70,175,'etudiant','student','PREREGISTERED',NULL,'0',10),(36,'nora.diouri@insa-lyon.fr','429a90c5429de9f514605a7e7d9d20bab51164e474c008f063270aa8c0693612:ed7f0d04a54d4617b004567fdd05da3c','Nono','Féminin','Nora','Diouri','1993-08-12 00:00:00',60,170,'etudiant','student','PREREGISTERED',NULL,'0',11),(37,'quentin.dupont@insa-lyon.fr','f8db2627a0285db14c9417b6bcf02afae79e9be7c86382929af31fe48ab8f011:88e27c0f1ef54250a420277a1fa7b5a0','qdupont','Inconnu','','',NULL,NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',12),(38,'thierry.barioz@insa-lyon.fr','f97123fee5a263795f61784800f0f4f411303ab801a6c9a72cf6a8a73e5fff65:8a1c5489c5534ad7a1eaf10c899d43aa','Thier','Masculin','Thierry','BARIOZ','1976-05-19 00:00:00',92,181,'iatos','employee','PREREGISTERED',NULL,'0',14),(45,'annick.cortay@insa-lyon.fr','61d5ab63c903b7991a35add35a666d9ca40602168607d226f4f51ad21746358b:5a4ac98efc1f417583f20cd7aab0ada2','Nikette','Féminin','ANNICK','CORTAY','1958-08-29 00:00:00',78,165,'iatos','employee','PREREGISTERED',NULL,'0',15),(46,'marie.dandrea@insa-lyon.fr','bf712a84b042e1bef497d676cec610d12bb182b6f7ccaf9e41c7e8b16aade0a2:c83bf3a8a52a47daa2a8bbd4f083b40a','nenette','Inconnu','','',NULL,NULL,NULL,'iatos','employee','PREREGISTERED',NULL,'0',16),(47,'damien.fabregue@insa-lyon.fr','1b021df4a46cb79d5958d2791dabdd1e20bdd34bd7f79e0bc3db25205721fd6b:91b78edb69844662865700550edb6cbc','dfabregue','Masculin','Damien','FABREGUE','1978-01-21 00:00:00',72,184,'enseignant','employee','PREREGISTERED',NULL,'0',7),(48,'raphael.chassagnoux@insa-lyon.fr','44d5770ee894d54ce9128641bd6ab4f496782e42ada5166601af46ff213eb989:9f09a47da76848d4bac2722212aed3eb','RedPanda','Masculin','Raphael','Chassagnoux','1993-08-27 00:00:00',60,178,'etudiant','student','PREREGISTERED',NULL,'0',13),(49,'tongjia.liu@insa-lyon.fr','a084b87106413e22e391ab746583157ab6840d9f45e5367019cd704502e101e7:dd904ec3f56d45d39ed9cd98394343d7','TJ','Masculin','TongJia','LIU','1993-08-02 00:00:00',70,188,'etudiant','student','PREREGISTERED',NULL,'0',14),(50,'patrizia.peller@insa-lyon.fr','9c5e4c82e58a63338f00ffb82ab2c60ab42772b8b7250cfd9a96498527867f0a:eedca7e1d6cd4011a0bda7ad8b210d08','Padi','Féminin','Patrizia','Peller','1990-08-18 00:00:00',50,160,'etudiant','student','PREREGISTERED',NULL,'0',15),(51,'jean-paul.lubamba-tshibwabwa-nzuzi@insa-lyon.fr','8a71eb7eeca6c9d9a51300dbb359d0ebc38ea9e29aff66b408b897e4605ec07b:f0eef2b26f244c0cb5a31b17898ce93f','JP','Masculin','JEAN PAUL','LUBAMBA TSHIBWABWA','1969-10-10 00:00:00',83,180,'etudiant','student','PREREGISTERED',NULL,'0',16),(52,'joelle.jaillet@insa-lyon.fr','d6973af72508f831ebf7a985e583d27f0d20748ee0b49841b9aaf765d5a15d56:6409feff4fa44ef68c9e5d818f10499f','jj','Féminin','Joëlle','JAILLET',NULL,49,154,'iatos','employee','PREREGISTERED',NULL,'0',17),(53,'odile.richaud@insa-lyon.fr','a6064bfb3679a896f97cd88cf15a20b5c494be46dfa2bddfb72631a36e44d9be:e7bf2a05a4ea467bb993f130f5733ce1','Chartreuse','Féminin','Odile','RICHAUD','1964-12-29 00:00:00',70,165,'iatos','employee','PREREGISTERED',NULL,'0',18),(54,'pierrick.merino@insa-lyon.fr','c4fa6f5ee0c5344fc403e01d3bfb54f2aa5bf30c25798982bb7fb903652602cf:a01af8ab537a459e9e0e5193cc99bd90','Pierrick','Inconnu','','',NULL,NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',17),(55,'guillemette.trognot@insa-lyon.fr','bb2eba390adb4991e28d52afebfd40edf8a94fe27baeff9c7d87b5077bd6f052:59983aa6c8304baaa3d4f6101c41368e','gtrognot','Féminin','Guillemette','TROGNOT','1972-10-27 00:00:00',82,160,'iatos','employee','PREREGISTERED',NULL,'0',19),(56,'christian.loyalle@insa-lyon.fr','a9c9dbd555116bf56e27c2710015bc51604ca2794ea6974a31a91efdaa79238b:4ee492b8201e4feda4885053e50e8a96','denis','Masculin','CHRISTIAN','LOYALLE','1965-02-26 00:00:00',78,172,'iatos','employee','PREREGISTERED',NULL,'0',20),(57,'raymond.cortes@insa-lyon.fr','c33497300e11f2c591703b212ee466cd9d8de3e2bbb4108b9479de41116365e2:60d32f52fbcf4ef3b0a10cd9ab5dfc52','raymond','Masculin','raymond','cortes','1955-03-17 00:00:00',75,183,'iatos','employee','PREREGISTERED',NULL,'0',21),(58,'patricia.guilliot@insa-lyon.fr','3c86a011dc4bf753715d7377264458c11056dfcf38c42b8fc269190874cd51c6:be90837627064e25a619536aa739889e','Patsy','Féminin','Patricia','Guilliot','1957-08-29 00:00:00',70,NULL,'iatos','employee','PREREGISTERED',NULL,'0',22),(59,'sadok.gharib@insa-lyon.fr','66305dc6ee5aa531e0564164fcf8f268aa60cd8e4523bbb957f64e4a8611700e:34f858022e0b4d84b8ef0d0f1ad48db9','felin','Inconnu','','',NULL,NULL,NULL,'iatos','employee','PREREGISTERED',NULL,'0',23),(60,'anna.loehr@insa-lyon.fr','2001c994c351d21bc9b49731cb3235a843e8c5f0113e264ea7f87b526743e59d:8ae4046c4817476ebb3bd29d50def5e6','Anna Loehr','Féminin','Anna','Loehr','1986-06-14 00:00:00',54,170,'iatos','employee','PREREGISTERED',NULL,'0',24),(61,'armelle.vidal@insa-lyon.fr','c10b3d0378fdd4771bacc6a6454740e8bdcb6c878b4cd6971ea382d2f1537672:de8d0112c4c24c69ac4bdb43a11c0b6c','Armelle','Féminin','Armelle','VIDAL','1989-03-31 00:00:00',52,160,'iatos','employee','PREREGISTERED',NULL,'0',25),(62,'francoise.georges@insa-lyon.fr','7e39d9c4e0a5ab8cdba25e189d2e4766d5d62e6a5d8b5fbf7f8a9c44677ea8a8:267a7834b4404bd18ee0de88d1c6c970','souazic','Féminin','Françoise','GEORGES','1962-04-18 00:00:00',75,163,'iatos','employee','PREREGISTERED',NULL,'0',26),(63,'fabien.mandorlo@insa-lyon.fr','349e35c043579f8b4229bc977d2cdd026ca139ead33bd52d0bef13f8fae0f045:6ca7fb1c0aec4909b0a7a999f9e0cbfc','DayWalker','Masculin','Fabien','MANDORLO','1982-02-12 00:00:00',88,170,'enseignant','employee','PREREGISTERED',NULL,'0',8),(64,'mathieu.bouyer@insa-lyon.fr','db00d34a01e2752f3e6fa30371de7619c669d380da4f6b11753ecea6ed4532d0:71fec4413a8046338511de2c80574b91','Achille','Masculin','Mathieu','Bouyer','1978-03-01 00:00:00',72,180,'iatos','employee','PREREGISTERED',NULL,'0',27),(65,'jean-baptiste.boni@insa-lyon.fr','cf67b239eab1e9e9f589859357b18a3e23bc37ae5604e0535e711f80ccb34de2:b222ca5592064a669621a3c727eabc3e','JB','Masculin','Jean-Baptiste','Boni','1993-04-23 00:00:00',72,175,'etudiant','student','PREREGISTERED',NULL,'0',18),(66,'pascale.canivet@insa-lyon.fr','84dbd5c58164fecd37974f38b5963e6922c798ac558134384c83ac8b452cc162:3433e4f06eb544e6bee77c03c5495111','pascale','Féminin','Pascale','CANIVET','1959-02-02 00:00:00',61,169,'iatos','employee','PREREGISTERED',NULL,'0',28),(67,'olivier.merchiers@insa-lyon.fr','156447f753cc08a57fd0b3ccca89c29f7fada9dbf8bf2a04850e42c8fa746b6f:69d6c4a8950747f3af29a9f5a9587737','Oli','Masculin','Olivier','Merchiers','1978-06-08 00:00:00',73,178,'enseignant','employee','PREREGISTERED',NULL,'0',22),(68,'lorraine.trilling@insa-lyon.fr','f57fa347c1ff06e32490d56149bda092db193d06495cd2b2147b417737b71cb3:abd2a5eb9c0f45e794945545f98c2a38','trillingtrilling','Féminin','Lorraine','Trilling','1981-08-06 00:00:00',45,160,'enseignant','employee','PREREGISTERED',NULL,'0',10),(69,'corinne.subai@insa-lyon.fr','5469fd30279dcce3c17879bbe70b37d8736dd95146038c3f84bf1447fafb7d91:b939b65c4c89412fb85a7c69520e071b','Coco','Féminin','Corinne','SUBAI','1970-09-17 00:00:00',98,177,'enseignant','employee','PREREGISTERED',NULL,'0',11),(70,'antonin.fauret@insa-lyon.fr','c1f7c1c3bf56d6916b5ff695114970aed2469c8015eaf2b5bbe65a2d32558fc5:9dcb5fea72b849c197f39e91720c840a','Anton\'','Masculin','Antonin','FAURET','1994-08-25 00:00:00',54,175,'etudiant','student','PREREGISTERED',NULL,'0',19),(71,'sebastian.sandu@insa-lyon.fr','93ee23fecb8d29ec017df57fe992498a5ea13632314b3853c460377118ad7b56:8427a0ed4a0f495180c10363231d6322','Zorro','Masculin','Sebastian','Sandu','2016-02-29 00:00:00',300,91,'etudiant','student','PREREGISTERED',NULL,'0',20),(72,'marie-paule.voita@insa-lyon.fr','b71c9a2a5cf5fc9e9d4b7bf2ccb10548fefe12746dfdc8a858ad106d821bbc21:352e4d7c1a2040aebe61d7b8a63e7095','mpv','Féminin','Marie-Paule','Voïta','1955-11-07 00:00:00',55,160,'iatos','employee','PREREGISTERED',NULL,'0',29),(73,'jacobo.levy-abitbol@insa-lyon.fr','8221d703a216b9426a2e8966f28041d524c140b212ab840bffd5f03fb3ed9b74:5633484c13d443e79f1d215d02a70fdf','zuz','Masculin','Jacobo','Levy Abitbol',NULL,NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',21),(74,'dalila.boudia@insa-lyon.fr','a7fe96812ca3ac695a97b6f82942d60c603887e936bdea6a627a1c52f00a77f9:ddca7d68de3d4b03a42009586206a0d9','lilou','Inconnu','','',NULL,NULL,NULL,'iatos','employee','PREREGISTERED',NULL,'0',30),(75,'anne-marie.clement@insa-lyon.fr','8560a34ff4573d18f3c9fae3af2735c92dc894758945a80d581ed29dfcb26879:075d391892ef43498122b1b298ca51e0','Wood','Féminin','ANNE MARIE','CLEMENT','1966-04-09 00:00:00',55,166,'iatos','employee','PREREGISTERED',NULL,'0',31),(76,'sandrine.forichon@insa-lyon.fr','1b267564a19495102520260649a32ba794ea07186632de7192d7c2c1b217035c:d239782badce41abbcc5f6454e679cee','Sandrine','Féminin','Sandrine','Forichon','1973-01-05 00:00:00',50,165,'iatos','employee','PREREGISTERED',NULL,'0',32),(78,'francoise.chesa@insa-lyon.fr','8edaaf80b3ddbe329a668dcff50dc7d90274631f6fa652e5f26007e9cab891c3:03bc2af6b1984bfe8e3c6d06b5c875ea','Françoise','Féminin','Françoise','CHESA','1964-05-31 00:00:00',73,174,'iatos','employee','PREREGISTERED',NULL,'0',33),(79,'mallory.felix@insa-lyon.fr','74ca23dfd2223b61d47770be160a2e53dabbc7f3cd1de8fbd9b49415694007df:cb0ec5181c504688a518ea62595a531e','Mallo','Féminin','MALLORY','FELIX','1974-10-24 00:00:00',50,160,'iatos','employee','PREREGISTERED',NULL,'0',34),(80,'maria.baboulall@insa-lyon.fr','4de947de6424a17f0332361ba702f0563f63deb30d7453458660d88374ad4810:89046ac45b4c4e2e8370f45723cdd984','Mariia','Féminin','Maria','BABOULALL','1993-04-14 00:00:00',NULL,169,'etudiant','student','PREREGISTERED',NULL,'0',9),(81,'thomas.losbar@insa-lyon.fr','019fbd6a54ed7d32d5510f220fae75af4bda69c37ba40cd9a43a1746cabc5e28:b58d2576442e477794f2cdf457cef76f','Jaf270','Masculin','Thomas','LOSBAR','1993-07-24 00:00:00',55,169,'etudiant','student','PREREGISTERED',NULL,'0',23),(82,'julien.courbis@insa-lyon.fr','25f48e4583ae88ff91b40afcdd92e18aeb3a45dbe7c8a886c68bd3bb12e6fb98:dce6b93f78e044edbdff720c7b580b08','Rulio','Masculin','julien','courbis','1994-10-30 00:00:00',70,180,'etudiant','student','PREREGISTERED',NULL,'0',24),(83,'camille.fayand@insa-lyon.fr','d1338fa369337ec246eb06637c260e9edb106fdfacf3cd0e01718241acdc9429:327ff99cc0054995aad1d81a15c62faf','Mono','Féminin','camille','fayand','1994-04-14 00:00:00',53,153,'etudiant','student','PREREGISTERED',NULL,'0',25),(84,'corentin.nelias@insa-lyon.fr','0419611be481b55dbd5af804675f44ec00d7c93b4cb1679b3f945bebd0db4894:0495f0465a374b218e59dc3618411abc','cwok','Masculin','Corentin','NELIAS','1994-10-13 00:00:00',87,192,'etudiant','student','PREREGISTERED',NULL,'0',26),(85,'emilie.pichot@insa-lyon.fr','322636a91953d60b74d274a16221f72b4eeece44d05a424a65463e16d8589555:235d6290c7914b809e4078b2f947978c','Mimie','Féminin','Emilie','PICHOT','1993-02-15 00:00:00',58,163,'etudiant','student','PREREGISTERED',NULL,'0',27),(86,'emilie.robert@insa-lyon.fr','e747c40a9a7e1dd337b8d21b9e2d4af2156c84423a015ccf5db22b066dc44502:932d20af8c4a48aab6a534d7a363b859','Mimi','Féminin','Emilie','rOBERT','1994-11-21 00:00:00',67,164,'etudiant','student','PREREGISTERED',NULL,'0',28),(87,'Bassma.alhamany@insa-lyon.fr','25ee59aa3096bf8643e64e40463c3ff185c081bad7a23e445136cf35143cd308:52211a06edf444a8ac9a88e2c98329c0','Bassoute ','Féminin','Bassma','Alhamany','1993-12-03 00:00:00',49,154,'etudiant','student','PREREGISTERED',NULL,'0',29),(88,'hoang.nguyen@insa-lyon.fr','070e75ea1bccd8cc951da1690fb065c7ff3889f7c274e534c5a478ab7de7c461:46f688847b624cc1a022b74f756a8d07','Mountainking','Inconnu','','',NULL,NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',30),(89,'esther.cagnin@insa-lyon.fr','6fd69f55a940b4e71e6ffc253e388a34a32aab8ea1b28846381817aa730147ae:ba56781b889047578f29036690015328','Esther','Inconnu','','',NULL,NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',31),(90,'berthold.mader@insa-lyon.fr','d5a609ca1c062e8bd6785546703e7798ddb7d18e5d18669575d7b34420f1d78b:24a05e97617f4551a6faf089eef36d8f','mons','Masculin','Berthold','Mader','1955-08-19 00:00:00',70,169,'enseignant','employee','PREREGISTERED',NULL,'0',12),(91,'mireia.miralles-i-castaldi@insa-lyon.fr','2b1e68336e3233f706d06b588c8627f6cc9693cc2d516bcc599258c5689c8960:6283b791d2a34ffd96423778bd0372e5','mireiamrlls','Féminin','Mireia','Miralles','1995-06-07 00:00:00',60,159,'etudiant','student','PREREGISTERED',NULL,'0',32),(92,'liviu.militaru@insa-lyon.fr','912323381f1c757e23cb5d15948ffc7d072392071eaa849998b8dfc665769724:9b6cffd7837d4c08be306bd5ce8b0fe7','LM','Masculin','Liviu','Militaru','1974-01-08 00:00:00',87,180,'enseignant','employee','PREREGISTERED',NULL,'0',13),(93,'lara.casiez@insa-lyon.fr','6d1bc757128ed37a630a5f6f9772fc07c96dd76f500d6fd752572d63c61d9ad9:9363cb52ea7647319ff75638dce7cea0','Lapalou','Féminin','Lara','Casiez','1995-06-28 00:00:00',60,172,'etudiant','student','PREREGISTERED',NULL,'0',33),(94,'francois.robion@insa-lyon.fr','68c40cbc2764cec726e74aa125718f8a62ae3a21ed5ed7375d73ad777bb5ab60:7fa71293791940e8960ca508c7f5970b','matrop','Inconnu','','',NULL,NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',34),(95,'Cindy.caccavale-ojeda@insa-lyon.fr','404efc4a1d42ddb2a9655977e15fcbdb0b21d0bbb4fe78f54078a78dc3f5357b:5f2d421cc2c44f6982bbfbe2f6f00428','Chindy','Féminin','Cindy','Caccavale',NULL,NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',35),(96,'pascal.chiu@insa-lyon.fr','d2ba7e37667f479f126d9be28973a07f590644388b1da4bc19137189cf5ce532:541061b300c9484485652d5161bdc3ba','KuronoSe','Masculin','Pascal','CHIU','1996-07-22 00:00:00',NULL,189,'etudiant','student','PREREGISTERED',NULL,'0',36),(97,'pascale.stephan@insa-lyon.fr','c238cb5c60dab8176e27127e836be8e30d109366fb5dd6969cc3e7d74718e402:3cbf43c8c2d94f62963fde61b9eadfe1','zitoune','Inconnu','','',NULL,NULL,NULL,'enseignant','employee','PREREGISTERED',NULL,'0',14),(98,'lara.chevallier@insa-lyon.fr','7d880a9f11d56c875796606dfa1c13f5ccb6fc6b6d37d86ef2a17294982f7e56:a436359dcb2c4f64be0620ac8a8219d4','Lara','Féminin','Lara','Chevallier','1996-11-14 00:00:00',NULL,169,'etudiant','student','PREREGISTERED',NULL,'0',39),(99,'Mathieu.Maranzana@insa-lyon.fr','24c00f4d8860236178396a999eeb57c02370abad439c1c82331b1414bec73982:4bf239e5b67749199f2b810c2d82d414','Dadello','Masculin','Mathieu','MARANZANA','1963-09-02 00:00:00',98,190,'enseignant','employee','PREREGISTERED',NULL,'0',15),(100,'marc.aubry@insa-lyon.fr','55cfe425fa788f4c3c6a3c051908c58b2a318288fc24537505f4d460aca36d3c:e955b6a5891846c38d70787b4a229da9','marcus','Masculin','','',NULL,75,190,'etudiant','student','PREREGISTERED',NULL,'0',38),(101,'guillaume.marie@insa-lyon.fr','f8257078e820dc1dfa65c030243e77c515482987246cf8d542373acbee790d8a:d245b46d89f84d5e8f7eb92b6510ae14','Guigui','Masculin','Guillaume','MARIE','1995-11-10 00:00:00',72,178,'etudiant','student','PREREGISTERED',NULL,'0',37),(102,'nadine.noel@insa-lyon.fr','00608de92955e4a7cb6bbf5a3deaaff088bebe6e7008858370c1f5c3beb4cb49:9248d05aea874c499cbdbfa2ab05426b','Nad','Féminin','Nadine','NOEL','1974-09-15 00:00:00',56,160,'enseignant','employee','PREREGISTERED',NULL,'0',16),(103,'marie-pierre.favre@insa-lyon.fr','0456e963b28940a7dae32354e3899c28b39981137c860e58fde84647643aba76:5397fb7df6374922ac35cfab45662032','marche','Inconnu','','',NULL,NULL,NULL,'iatos','employee','PREREGISTERED',NULL,'0',35),(104,'thomas.monnier@insa-lyon.fr','a66a68b742e45dff242041b58c826be0ff306ed2f8fa273b994400410f26ae87:e5c5b5fb5373485791a4392bc7fdf167','tmonnier','Masculin','Thomas','Monnier','1974-03-05 00:00:00',62,167,'enseignant','employee','PREREGISTERED',NULL,'0',17),(105,'thierry.moyaux@insa-lyon.fr','9222b83f1d421da824208b4c74e6b5d3c82fd410958a2c805e3bc9a88f289786:38c655af01e74b60b9a4ac7abdf8ddd8','moyaux','Masculin','Thierry','Moyaux','1977-07-21 00:00:00',71,177,'enseignant','employee','PREREGISTERED',NULL,'0',18),(106,'Marian.Scuturici@insa-lyon.fr','2713d9403aa7a2484e04bca8d5e972fead14c9ac876a59deb805c1ec64009a4a:cca05a851efd48319e7f7030b7335477','Marian','Masculin','Scuturici','Vasile-Marian','1971-10-30 00:00:00',100,186,'enseignant','employee','PREREGISTERED',NULL,'0',19),(107,'gang.cheng@insa-lyon.fr','21817af2d7ba5942fca4b388ac6b7bbce39e4d860442e37debdf1553f80ef5c1:ec10fb3e8f9c4f81a706a86f54ed4d02','Gang','Inconnu','','',NULL,60,175,'enseignant','employee','PREREGISTERED',NULL,'0',20),(108,'valerie.flecheux@insa-lyon.fr','b266074e64d7ba45f7f68e1420b0f71de552c7f9cd70ab9d63ea76606a261c91:53c7bb048e4540b0b52d509713dac9a0','Val','Féminin','Valérie','FLECHEUX','1973-09-12 00:00:00',58,173,'iatos','employee','PREREGISTERED',NULL,'0',36),(109,'emilie.chaume@insa-lyon.fr','f8f5c0f93c25a8ffff868d3f17012f79bb6a211dde0d108728afe2fe86aaa554:85375cb38d0e41d090776f27011b326e','Emilie','Féminin','Emilie','Chaume','1993-04-06 00:00:00',47,160,'iatos','employee','PREREGISTERED',NULL,'0',39),(110,'serge.kingue@insa-lyon.fr','e83103cacdc8584998e81795cc2391fd5fe0d4e75385979fd29c590ecb1a3bc3:e2ba338300984817b6e5dc640c353b03','Sergeos','Masculin','Serge','Kingue','1990-06-11 00:00:00',117,190,'etudiant','student','PREREGISTERED',NULL,'0',40),(111,'matthieu.rollain@insa-lyon.fr','fe4fd7a82a990add1aac71aa8b8f9a9b1b38a998889b6f0c532f2dff7abea30c:7ab183056f654746891aa942dfa5522b','Gary','Masculin','Matthieu','Rollain','1995-11-21 00:00:00',72,176,'etudiant','student','PREREGISTERED',NULL,'0',41),(112,'vincent.ollivier@insa-lyon.fr','763153719d7e581bac8ea01979dfb975ef3d486d224d5540facc0b7930fd591e:e16f422455594dc3a57f22b673df28ab','Vinc05','Masculin','Vincent','Ollivier','1996-05-03 00:00:00',60,174,'etudiant','student','PREREGISTERED',NULL,'0',1),(113,'marine.minier@insa-lyon.fr','6de0791695797d918f6dc7d298211dac02052a39cd2de892d634bcfa09e5cad4:6ae4a5171bef4e07b2c2d3a8b131a4f4','Marine','Féminin','Marine','MINIER','1976-01-28 00:00:00',75,165,'enseignant','employee','PREREGISTERED',NULL,'0',21),(114,'isabelle.naveau@insa-lyon.fr','dde535d1e870f0768d4bacfc5ccc45e724bf42f1708070ccb5e6049e0c5c4451:56e11ab968624cc38ed45e99fd312bc6','lilote38','Féminin','Isabelle','PETRIZZELLI','1969-09-23 00:00:00',62,159,'iatos','employee','PREREGISTERED',NULL,'0',38),(115,'apolline.pibarot@insa-lyon.fr','5eafe7b978a78ceca591b7ae38ea1e83f48ae258ab2dd667de6a43d055960864:f7fd723c395e435db08eccc8b5efae1d','ZamZam','Féminin','Pibarot','Apolline','1996-11-19 00:00:00',50.5,157,'etudiant','student','PREREGISTERED',NULL,'0',2),(116,'maelle.seigle@insa-lyon.fr','a34350d75fcd447a1745354be9dc1134cdbefe9bed9116fd80a45afb7d4a883d:10602a17cd2c4214987e91468aa674df','Malou','Féminin','Seigle','Maëlle','1994-07-28 00:00:00',NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',3),(117,'chantal.berdier@insa-lyon.fr','cc60275f176f8fd8f64b51c9f96bbc6f683301fb0a96415dc3e69ddd80b76733:baa367a71930457ebc61ca10cff70095','Diana','Inconnu','','',NULL,NULL,NULL,'enseignant','employee','PREREGISTERED',NULL,'0',9),(118,'raynald.richard@insa-lyon.fr','89ce9793ccca0e71b829afd1265bb163466c5e8567b114902ff516bfc2d752f1:c20bfec33ba4448b8b2024a83870a336','kostas','Masculin','Raynald','RICHARD','1975-05-20 00:00:00',77,176,'iatos','employee','PREREGISTERED',NULL,'0',37),(119,'marie-madeleine.deguin@insa-lyon.fr','8ddaa133dbc0da0daed55483b35db61710fe4f991640941f0c72faa956a86885:a820309c82dd441aab7fd517a7f67740','bobo','Inconnu','','',NULL,NULL,NULL,'iatos','employee','PREREGISTERED',NULL,'0',40),(120,'soline.gautier@insa-lyon.fr','ead8f52c5fb21062e383f0fa6ceba1d09441f3c54ba75e4a90b50005b1cc92ec:6795fab555e2489cbef2e74c308bf341','Stitch','Féminin','Soline','Gautier','1995-07-09 00:00:00',NULL,170,'etudiant','student','PREREGISTERED',NULL,'0',4),(121,'okba.khenissi@insa-lyon.fr','1ee1fccb6a265853f351473e3a837d6edc54d271ca0213797f6b6ef0a8040923:6d780a0dc2b34111b3ef28035b82442d','ammouZayd','Inconnu','','',NULL,NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',5),(122,'irini.djeran-maigre@insa-lyon.fr','e92948a574d953d732d15a17d2cc60facdddf4f6f50da28534d04a8e54edc111:c164161267254798abc2d2262446edfb','Athlos','Féminin','Irini','Djeran-Maigre','1959-02-19 00:00:00',NULL,NULL,'enseignant','employee','PREREGISTERED',NULL,'0',23),(123,'frederique.biennier@insa-lyon.fr','6a0a77964e5aa53eecc3284f34547ec98ccbb10b05164b706360b4829bc8127c:02eacf1b15244afaa73aff1129dcdaca','fbiennier','Féminin','','',NULL,NULL,NULL,'enseignant','employee','PREREGISTERED',NULL,'0',24),(124,'hamza.aoutil@insa-lyon.fr','8e75c1ee68e638ecd89d8eaa1fbbf4435ae5c5db16ea1f6f30fd0d8fdc6e7b42:c721984ea2e5478698533c24ea012ccc','momo','Masculin','hamza','aoutil','1991-10-13 00:00:00',75,170,'etudiant','student','PREREGISTERED',NULL,'0',6),(125,'nathaly.berthillon@insa-lyon.fr','4ca6f7ab53f8878f6efe5e2978b2321ffb7a324a2407f91fb83b9d4f713a729d:b90e947fcaad4314bca8eedeb68ff707','BN','Féminin','Nathaly','BERTHILLON','1964-06-12 00:00:00',52,165,'iatos','employee','PREREGISTERED',NULL,'0',41),(126,'sami.debbache@insa-lyon.fr','562d79a34b7b96d2fb3615809b962c175136ea4410492e8f118af1e6aec7ca98:878026d029c843e3a75ea1260fce44c2','Samou','Masculin','Sami','Debbache','1993-03-23 00:00:00',83,183,'etudiant','student','PREREGISTERED',NULL,'0',7),(127,'michael.barbier@insa-lyon.fr','8ef6f27818b25ffbf78c41a74451f0854a9bee7536407ee243c69c7887d5114d:8ff1862ad2ff4d23a5f7dfe578acb202','Michou','Masculin','Michael','Barbier','1993-01-02 00:00:00',75,177,'etudiant','student','PREREGISTERED',NULL,'0',8),(129,'quentin.wolffhugel@insa-lyon.fr','cdd7b1f1b95bf52aeee298aa61fef0c84f3f26219d6e47b443871258dc28f5a3:3629f1978d90492f981909d92c1363af','Wolff','Masculin','Quentin','Wolffhugel','1994-03-03 00:00:00',75,185,'etudiant','student','PREREGISTERED',NULL,'0',9),(130,'christophe.berthier@insa-lyon.fr','507b6b21f68e9f7069721f99ab10cbd639a6d2280e23d8dfa6b1ecc78c0e7b2e:92a72c72e16b4670909f66764b433f54','Douglas Green','Masculin','Christophe','BERTHIER','1978-01-07 00:00:00',95,175,'iatos','employee','PREREGISTERED',NULL,'0',19),(131,'marjolaine.dudouit@insa-lyon.fr','521b808755eb9cbdeda8e9067571e601f9c1e32d1a07c84eadfea1a495fb24ab:cc33c97380774d4098bef1d56256df96','Mayo','Féminin','Marjolaine','Dudouit','1994-09-03 00:00:00',66,171,'etudiant','student','PREREGISTERED',NULL,'0',10),(132,'arthur.faure@insa-lyon.fr','a704cdef35cef430e81ec1aa5b6bcb831ab216a00a5617dea3073bb65fd21054:95020f1b012b4efeb01326dc2a483c99','arcthur','Masculin','Arthur','Faure',NULL,70,183,'etudiant','student','PREREGISTERED',NULL,'0',11),(133,'sandrine.gonnet@insa-lyon.fr','4d9010833983c7054f15d3dbb32bdf2da2318bb628280aa26f3916d939f50f9a:b9aa9174235f41e9a61aff2e81a3583b','Sandy','Inconnu','','',NULL,NULL,NULL,'iatos','employee','PREREGISTERED',NULL,'0',20),(134,'didier.remond@insa-lyon.fr','31e178da890d306ccae9576534febe8c2d63ebac3e5c4d6be63f21e042668f3b:ddeafd2b3e6f44899d77053a14e39b22','Didi','Masculin','didier','REMOND','1964-08-29 00:00:00',78,178,'enseignant','employee','PREREGISTERED',NULL,'0',25),(135,'marguerite.duboz@insa-lyon.fr','2880119bf99ed6e03af4874a8c9defd039c43b17c247392feae83c52330b26e8:41b8026d99804b10b570bc02ce7b88cc','kaya','Féminin','','','1959-02-19 00:00:00',NULL,NULL,'iatos','employee','PREREGISTERED',NULL,'0',21),(136,'nadia.bensenouci@insa-lyon.fr','822c8952d695a0d25ccd9bda05b3c736c5695977cca9f3c6c8a0bc04a09624cc:fb7136628a9841748fca1c200d49d103','nadiab','Féminin','Nadia','BENSENOUCI','1968-10-26 00:00:00',70,168,'iatos','employee','PREREGISTERED',NULL,'0',22),(137,'laura.paget@insa-lyon.fr','e186c992bc6f6c0ea80847a707dfe21c4e21c66f64016779e6de03f92e6c1c49:b39cb526fea94dfb9dd8562f8a17a9c4','Laura','Féminin','Laura','Paget','1996-10-11 00:00:00',NULL,173,'etudiant','student','PREREGISTERED',NULL,'0',12),(138,'manon.monfort@insa-lyon.fr','5b97104cb1d40124daa407e87d8abe189922d854caa1aab32577f675eff94e86:fe8c80ca20944067bea8ccb2da328d3f','Manon','Féminin','Laura','Paget','1996-10-11 00:00:00',NULL,173,'etudiant','student','PREREGISTERED',NULL,'0',13),(139,'yann.gripay@insa-lyon.fr','be28cce73dddb50d6f0e69b7c305a0aef1a9846e56259feba2b0a315f4003773:d4830d2e42f4496c987a3f1021f2a55f','Yann','Masculin','Yann','Gripay','1983-12-18 00:00:00',85,180,'enseignant','employee','PREREGISTERED',NULL,'0',26),(140,'elodie.perez@insa-lyon.fr','4159510fcbc1561e1b57def960c1dccc0aa176415c87297696632460d3b0e9cb:26f5e9f3aa7a492f82bb12526d08c806','Elo','Féminin','Elodie ','Lascoutounax Perez','1981-07-13 00:00:00',NULL,160,'iatos','employee','PREREGISTERED',NULL,'0',23),(141,'nicole.goetgheluck@insa-lyon.fr','5227ca5ab218d4253da29f554ebd3144bd1c93b168f165bad88910c1e7df6e89:04f05bb6e43b4740b3b22525782610c4','ndevillard','Féminin','','','1961-09-14 00:00:00',49,163,'enseignant','employee','PREREGISTERED',NULL,'0',27),(142,'jeannette.buzzoni@insa-lyon.fr','2178b43b0956aea7ee3363f83f277167ab3022e510b108c5439f45d042d2eaca:2c3fd9bd6a2043c78621ac38ee15d672','janet','Féminin','jeannette','buzzoni','1987-12-19 00:00:00',67,173,'iatos','employee','PREREGISTERED',NULL,'0',24),(143,'camille.spigolis@insa-lyon.fr','8b035bf6274f5573fa1df22752a0ace4f33a85719e2a73f78986600c79d8ea72:c3990c634fc84be0be8ac7aeb0c73777','Spigo','Inconnu','','','1990-04-19 00:00:00',45,156,'etudiant','student','PREREGISTERED',NULL,'0',14),(144,'dominique.dumas@insa-lyon.fr','925c14a1cd03a0996a960b36eacc6484506cbc23e563cdacd375b29c049f6d89:17dc2ec4676b4ed4bba27dd21aaecd6e','domi','Féminin','Dominique','DUMAS','1959-10-08 00:00:00',68,157,'iatos','employee','PREREGISTERED',NULL,'0',25),(145,'marie.skopeckova@insa-lyon.fr','48da7376427555b7d292a86bb09b6662d5a58cc1b5d266090d7b4f0405b8e11d:f91e459210cd4ed9986ce8aefba65fbf','Magda','Féminin','','','1953-04-08 00:00:00',63,174,'iatos','employee','PREREGISTERED',NULL,'0',26),(146,'wilfrid.marquis-favre@insa-lyon.fr','16121f4c22d0a575da2edd53b6ebcc6ad21b99539745086424916ddd545e7da7:b60a242ce6754cf3a591bbf80f7969a7','Willy','Masculin','Wilfrid','Marquis-Favre','1968-11-23 00:00:00',79,178,'enseignant','employee','PREREGISTERED',NULL,'0',28),(147,'claude.guedat@insa-lyon.fr','1f8de99bbda1cd59570165dcacbd0c5647282ec4800903011c50cf9043d74f7c:b8c95d0fca5945bfb485ec65d0a300bd','Claude','Masculin','Claude','GUEDAT','1955-03-27 00:00:00',71,176,'enseignant','employee','PREREGISTERED',NULL,'0',29),(148,'emilie.baroux@insa-lyon.fr','6d61ee5c70fc0f6d5a532dcdc5588301e7513b4ca3b0294a8d1d7c7e18ada055:eb8cdde3aee44f52afb76331adf0437b','Milou','Féminin','Emilie','Baroux','1996-01-16 00:00:00',65,165,'etudiant','student','PREREGISTERED',NULL,'0',15),(149,'julie.ferret@insa-lyon.fr','ee1bd04358d13ab85977dfcfb0e4a302a0b2fe9729dc37bd653bf4b94da7ef94:68f239c4fe1845ff9964a134346dec98','Jul\'s','Féminin','FERRET','Julie ','1995-09-25 00:00:00',NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',16),(150,'corinne.dayeyan@insa-lyon.fr','e8aeddead59d5ff7a7151a21e334cedc5d24b125269c2449f28ac8f1955e3ada:ce3a304bde79439b868934576d687d07','dame Pépette','Féminin','corinne','dayeyan','1958-04-17 00:00:00',57,170,'iatos','employee','PREREGISTERED',NULL,'0',27),(151,'david.audigier@insa-lyon.fr','f4309fa5c358954fe961de2dd021593cd41bb515515df37ff00644d36f724ea8:26bb57472d574e3195beefb4066fadb2','barbalou','Masculin','david','audigier','1966-04-21 00:00:00',70,175,'enseignant','employee','PREREGISTERED',NULL,'0',30),(152,'mathieu.hamon@insa-lyon.fr','f2ad41e07566fc06be54597f1555b0c031076f915bb3ecf348e00f06978100aa:5ac3957688c246979fb358ff6547bca1','Matman','Masculin','Mathieu','Hamon','1995-07-19 00:00:00',75,185,'etudiant','student','PREREGISTERED',NULL,'0',17),(153,'quentin.bapaume@insa-lyon.fr','625ff2fa7fc240a1844f9311614105b865d3ebe7382a7fe51ec58baca09a8801:5b9d9b465e2146f2bd8d04a657ca623e','winnie moumouth','Masculin','quentin','Bapaume','1995-01-07 00:00:00',77,171,'etudiant','student','PREREGISTERED',NULL,'0',18),(154,'jules.saada@insa-lyon.fr','fd60ef1cbfdd7165adaa92d2a0b01a9138f35693f2d11c78bf4784eb133726a6:2afd5c4bc1a44889a8f96c039d86750b','Julio','Masculin','Jules','Saada','1996-03-19 00:00:00',75,178,'etudiant','student','PREREGISTERED',NULL,'0',19),(155,'francoise.sandoz-guermond@insa-lyon.fr','8ebe6e70c950fc482dc6feca5f6d5aa3f6278a392369d6776c70ec58d2ffcc01:b9ca8e2ec50f4f84b10e96d5cb34557d','La_Petite','Inconnu','','',NULL,NULL,NULL,'enseignant','employee','PREREGISTERED',NULL,'0',31),(156,'laurent.pietrac@insa-lyon.fr','39c4b1e61572d2cbdba9a0dca07bd7df900353f634830dcd356d66b08c16b00b:27e60556d8254539ab4a9e91ec381872','lpietrac','Masculin','Laurent','Piétrac','1967-09-13 00:00:00',74,184,'enseignant','employee','PREREGISTERED',NULL,'0',32),(157,'pierre.salgas@insa-lyon.fr','eaa3a50028677f1af37f11ce4270d3b075012ff043085e943ef781b73c33e6de:c29e580cb04d49308b01acfd92f35355','psalgas','Masculin','Pierre','SALGAS',NULL,92,175,'enseignant','employee','PREREGISTERED',NULL,'0',33),(158,'chloe.vercruysse@insa-lyon.fr','423c1b740ac5980254f45928e12bdfcd7421305e340fbea6d1511518373f2738:0a56860371f74531badb767cbc044541','Chloe2811','Féminin','Chloé','VERCRUYSSE','1995-11-28 00:00:00',NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',20),(159,'patrick.fagan@insa-lyon.fr','36b8b40edc8fb368ea65a9cc7182286823f82d7118581c0e18ed2452122a130e:c82a38f3c2f84e1bb89f96d65765b0fe','Pf441','Masculin','FAGAN','Patrick','1994-10-02 00:00:00',69,180,'etudiant','student','PREREGISTERED',NULL,'0',21),(160,'laurie.sordillon@insa-lyon.fr','304a2a8c5ed977e472c51832edbf3fd9cb4161b2150108315fcd78200b652f35:07084533ab2c40568d25429d21ff0e76','blondinette','Féminin','Laurie','Sordillon','1996-03-04 00:00:00',53,165,'etudiant','student','PREREGISTERED',NULL,'0',22),(161,'valentin.renault@insa-lyon.fr','debdeeea5fab589539ade874c3cbc5b9d6ff0c03445fce5576aeaed126f18520:d38367ccd1b84f438b158c54d1f0f85b','valou','Masculin','Valentin','Renault','1996-10-08 00:00:00',58,168,'etudiant','student','PREREGISTERED',NULL,'0',23),(162,'alix.lopez@insa-lyon.fr','8c681f2945c6fff7b44751714bd1a30aaddc7adde64525f5184b0b48f49736bb:d0c3961da4944a8bb757eac0665e7a14','Alix','Masculin','Alix','Lopez','1996-03-22 00:00:00',83,191,'etudiant','student','PREREGISTERED',NULL,'0',24),(163,'nathalie.follet@insa-lyon.fr','aba9f41c34199cb02e100b5168899a49ae6f1268af358730f975f8729f47bca4:5d8b6b88fd6a4d3cb5dfbf5f21c5d059','Svn650','Inconnu','','',NULL,NULL,NULL,'iatos','employee','PREREGISTERED',NULL,'0',28),(164,'frederic.arnaud@insa-lyon.fr','33f9a93a80d2f44050672fdd142fc163605dcbe17ffcaab43c6f1ab1908aa0f6:b81db0bbae834f9095a362f1095dfd7b','OSS117','Inconnu','','',NULL,NULL,NULL,'enseignant','employee','PREREGISTERED',NULL,'0',34),(165,'philippe.vergne@insa-lyon.fr','4be29b74056df706fae051e076be4f2ff8b942c0473f087f8e6503a8830c002b:d95c5384a1d14005a542e6073fbec783','PhV','Masculin','Philippe','Vergne','1955-12-15 00:00:00',73,185,'enseignant','employee','PREREGISTERED',NULL,'0',35),(166,'denis.chaise@insa-lyon.fr','8648afcc6ca838d030c8d90ad61b15bb83372a47159c47ffdf8c3e358ce20a45:9489f24adca34ea194051536ab9ab449','Dyono6','Masculin','Denis','Chaise','1957-07-20 00:00:00',88,183,'enseignant','employee','PREREGISTERED',NULL,'0',36),(167,'nathalie.bouscharain@insa-lyon.fr','f4ecfbaa76763909eb3230b0af94c0b016f9298cd0eaa910a93569c6865d4c7a:36f41ab2df8543a4a648fa404b102ff1','Thalie','Inconnu','','',NULL,NULL,NULL,'iatos','employee','PREREGISTERED',NULL,'0',29),(168,'andrea.accardo@insa-lyon.fr','2d54e4966f2d1b19321d6c50741604d692fe963193e2d980d6f644e72f9cd1ff:fe6fd5c0d261438c973be1512db658a4','Andri','Masculin','Andrea','Accardo','1993-11-07 00:00:00',63,170,'etudiant','student','PREREGISTERED',NULL,'0',25),(169,'eliane.roupie@insa-lyon.fr','885adcd15bf63dbc8eed7659bd9f86dc54f9eb428628e3434be3d9e7ccb9ba80:67e993071df1452d8d57b34e79797e61','Lena','Inconnu','','',NULL,NULL,NULL,'iatos','employee','PREREGISTERED',NULL,'0',30),(170,'pietro.li-volsi@insa-lyon.fr','8ef4f02d1dd326f28ed7e321427e9b1685c8a9d58793abe7050944610c7f0963:d560e6966023417888fe3c1ffa94a6de','pietro93','Masculin','Pietro','Li Volsi','1993-10-28 00:00:00',70,180,'etudiant','student','PREREGISTERED',NULL,'0',26),(171,'titouan.thibaud@insa-lyon.fr','cc24e3d3ebef71aeda6f06ddf1d79d6cc1ddba516097cf8658aa83692d244331:69c7b72706d941b8b4c218a055f0e3ec','Titouan','Masculin','Titouan','THIBAUD','1993-09-07 00:00:00',54,174,'etudiant','student','PREREGISTERED',NULL,'0',27),(172,'tiphaine.lheritier@insa-lyon.fr','b4853b6c5d844cfef066eb6fe7a026f42536f1f0b0272d404bfee8dbab19ea88:1a141cf8f04d47f593103d83f2dfd236','Tif','Inconnu','','',NULL,NULL,NULL,'iatos','employee','PREREGISTERED',NULL,'0',31),(173,'quentin.gardavaud@insa-lyon.fr','802e973bf8b6e5d5bf9bd9d70ec7d169d475c01129f82410c9edbf314e199374:d896982a3df34bdaae139db20aae056b','GuGu','Masculin','Quentin','Gardavaud','1996-04-26 00:00:00',63,176,'etudiant','student','PREREGISTERED',NULL,'0',28),(174,'tianyi.yang@insa-Lyon.fr','d77c4c1a92d79f2c0bd5a04a170495a13a37dba385ba19f870fbfa6b49a07842:a64c9ca35c3e427fbaf550d71ca3b781','Noah','Inconnu','','',NULL,NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',29),(175,'karim.benhmida@insa-lyon.fr','238c08e57690fef0aae110e99220798ba946ea6df0be021f0103f555ba5f8b93:488ccf3f77004d2bb0125524c540ee19','karim','Masculin','Benhmida','Karim','1993-04-29 00:00:00',NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',30),(176,'jad.oueis@insa-lyon.fr','89d00bbd1b1815714f40d1e8f4aae1a872c4a90c5be09b18737313f54e2630e2:a9b11668a5e5416f98efd14de14696f0','Jad','Masculin','Jad','Oueis','1992-11-17 00:00:00',NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',31),(177,'audrey.papin@insa-lyon.fr','4fdec44410595b8bbdfa1834703d96c749046e9c40add9d2de9e06cae8e5ed0a:1cd16414095942c8ab1ca031e6ae441d','audrey','Inconnu','','',NULL,NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',32),(178,'aigline.pahin-de-mostuejouls@insa-lyon.fr','027e315b664f2259b776df4b067052af20ec812bbd012c89a211dbbb63409d95:8b10fefc387d48c8868ba32d10bf6eb2','Aigline','Inconnu','Aigline','Pahin de Mostuéjouls',NULL,NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',33),(179,'tanguy.roux@insa-lyon.fr','c31551b219b505b9e47821d52d49f2e508f78e37fb4f5bd306bb8cd175e1fac1:175dae4f5daf4909adf9d5031a0f88ce','Tanguy_ASM','Masculin','Tanguy','Roux','1997-03-14 00:00:00',68,173,'etudiant','student','PREREGISTERED',NULL,'0',34),(180,'celine.robardet@insa-lyon.fr','9cb1e2b8c90c070c4aa67fac86e286e1c639a1dcf9fedcf22c19be89deeef76c:8ba6580e0a4f42d19c50cf5dc7149bbd','crobardet','Féminin','Céline','Robardet','1975-08-14 00:00:00',55,165,'enseignant','employee','PREREGISTERED',NULL,'0',37),(181,'nicole.vially@insa-lyon.fr','d962107bae29fd0372ccf4bd2fde725a1a63dec28a6cbe85249b7e4b53c53203:0b0e916ae71840dc8bb1a11e2ed8e4fb','Elocine','Inconnu','','',NULL,NULL,NULL,'iatos','employee','PREREGISTERED',NULL,'0',32),(182,'samuela.leoni@insa-lyon.fr','25ccf0e40bdd4ee44d8dac14b43e43a3a32e79f0cc5103a4e8e36068382632b5:9fe68fc0d92e48718bc8e85a03951e47','fragolina','Féminin','Samuela','Leoni-Aubin','1976-12-02 00:00:00',48,160,'enseignant','employee','PREREGISTERED',NULL,'0',38),(183,'elise.chane@insa-lyon.fr','469b4f7c2b695a03ddb5c319276c1aaf3e5c5fbe9fd63151ba506f5aed11c685:c7b458aa353444bea39ad906149eeea9','Aya','Féminin','elise','chane','1989-05-02 00:00:00',75,157,'iatos','employee','PREREGISTERED',NULL,'0',33),(184,'jean-baptiste.aubin@insa-lyon.fr','77692ce96a4b5ddd9176decf4d43dd7bcb82d63de0273daaa64301547f1f48ab:60fa341b76f043f39af95d773cc4e0f5','avesano','Masculin','Jean-Baptiste','Aubin','1976-03-26 00:00:00',80,175,'enseignant','employee','PREREGISTERED',NULL,'0',39),(185,'jeannie.jouffroy@insa-lyon.fr','adecbc320765cca9744b8e8c896b9b199fe673e840ba65c3542d8d811c4e6635:724e6f0978ee43d8b8c19f0218611700','Joz','Féminin','Jeannie','JOUFFROY','1959-06-13 00:00:00',63,173,'enseignant','employee','PREREGISTERED',NULL,'0',40),(186,'michelle.seignol@insa-lyon.fr','f6f8282524163f8fec6ea18f8bafd31bb35c331f6b1c46d83a38e3594e981c2b:72d0d715740849489cb6aff9e501679e','flora','Féminin','Michelle','Seignol','1955-01-08 00:00:00',60,165,'iatos','employee','PREREGISTERED',NULL,'0',34),(187,'philippe.lejeune@insa-lyon.fr','534b01797e9046651acc1fbe13c3f48704cfe090400e7cec5b2f98b6b7ae609a:c1bb9706e22b4a3ca7a4c5be459bbb32','Philippe','Masculin','Philippe','Lejeune','1954-07-06 00:00:00',107,188,'enseignant','employee','PREREGISTERED',NULL,'0',41),(188,'maud.breyne@insa-lyon.fr','074391f7839a87f2dc99b14b46e3c020b1b6fe6722ba6314a7071ddd7c7800e6:b6c7fa5553ef4538a62636009b754adc','Mo','Féminin','Maud','Breyne','1996-05-19 00:00:00',55,172,'etudiant','student','PREREGISTERED',NULL,'0',35),(189,'julie.coussy@insa-lyon.fr','8a70f420cdb9d25f8842388d4b1afbb09651091cc5aafdb4ca56d404c9d2c7ee:8f1d3bfd940146e2868f458b044bea2f','Couscous','Féminin','Julie','Coussy','1994-03-16 00:00:00',61,171,'etudiant','student','PREREGISTERED',NULL,'0',36),(190,'emilie.oustric@insa-lyon.fr','4b75fc3188bccf8fc4068378e3d2737541cac57227e749f1a236c7ecddf59a0c:f1119df1e45e422ca6651f2ccf2b4bcc','Emi','Féminin','Emilie','OUSTRIC','1993-03-14 00:00:00',52,170,'etudiant','student','PREREGISTERED',NULL,'0',37),(191,'cyril.fayard@insa-lyon.fr','d115c8940d789830552c9b29ea146ca74bbe22ce92b42385fc62af47240a1eaf:6dfb041d6c1e4e57a50cd30e55df7ccf','Cyril','Masculin','Cyril','FAYARD','1974-01-25 00:00:00',88,178,'iatos','employee','PREREGISTERED',NULL,'0',35),(192,'france.rebouillat@insa-lyon.fr','fb98e87ff6d2d6c230643925cbba70c4b9edb3ec4a977f6875f4285d31d7969c:cb7ac5e230bd4bbb8825f69586e0d4b8','Françou','Féminin','France','REBOUILLAT','1961-11-10 00:00:00',NULL,168,'iatos','employee','PREREGISTERED',NULL,'0',36),(193,'ophelia.rey@insa-lyon.fr','36db71aa68510bf7cac4db234b4b6a30e1fd35e5b95a214b36a11b656070d8ac:d4193430d75142f7a5f56f0e5207e4b9','ophelia','Féminin','Ophélia','Rey','1996-02-23 00:00:00',52,158,'etudiant','student','PREREGISTERED',NULL,'0',38),(194,'alban.martinez-delcayrou@insa-lyon.fr','39242715cf4ab8f0969e8574875266888812393a43b914a86910afb70d54e393:da273701d1764d8aa96603508c016aa0','AlbMD','Masculin','Alban','MARTINEZ DELCAYROU','1995-03-22 00:00:00',75,182,'etudiant','student','PREREGISTERED',NULL,'0',39),(195,'camille.godet@insa-lyon.fr','f89b9e4d76a6e134993979cebd5d4b809e67a7904a74167bc2c515505f7ade46:ec3283918cae43369f1ba456dd393f27','Camillou','Féminin','Camille','GODET','1995-08-26 00:00:00',58,167,'etudiant','student','PREREGISTERED',NULL,'0',40),(196,'elie.bretin@insa-lyon.fr','c4e6b4d96e07e75eb64e12c2a239b8e53760bf2576f670a1b9ce85aacc4a3680:38dc4d8105cf45fe91cefd5ed026e619','Eliebretin','Masculin','elie','bretin','1982-04-30 00:00:00',78,180,'enseignant','employee','PREREGISTERED',NULL,'0',12),(197,'christian.reichert@insa-lyon.fr','f4e477f888c5993720a97e343e99df0d773f38b7fe7ee1f50346e3edc7773e4f:65e31034a1fa4ec7b9d8e3f143489589','christian','Masculin','Christian','Reichert','1972-09-19 00:00:00',90,180,'enseignant','employee','PREREGISTERED',NULL,'0',13),(198,'julie.cheng@insa-lyon.fr','34fcf6f253848caebfe5cb7ef0427b99a282dd49dc74fded0d4311256befea3b:6da935d29b34455da535be1ffea71154','Crevette','Inconnu','','',NULL,NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',41),(199,'jingmin.guan@insa-lyon.fr','6f29f652b252a88cf97cc3cd091742b6d22523ca71ca7d242e38fe665b22b859:fbb9c6731712481e882fdbcb41d76c4a','Tina','Inconnu','','',NULL,NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',1),(200,'martine.paris@insa-lyon.fr','96cc56ca3af14b36bdd8bc90bd0d8b09407befbf8380bc7d2598fa9f3ddbc5f6:61811cf75d844aa480d6f60b60a4b41d','Martine','Féminin','Martine','Paris','1974-06-10 00:00:00',60,168,'iatos','employee','PREREGISTERED',NULL,'0',37),(201,'modou.cisse@insa-lyon.fr','251e800867a16a4a0854b54d1196e114f27dabc441210bf71cef6cc56b474715:e16325e00d3d47709e552186ebd1d755','Modou','Masculin','Modou','CISSE','1992-12-12 00:00:00',90,190,'etudiant','student','PREREGISTERED',NULL,'0',2),(202,'sandrine.richard-molard@insa-lyon.fr','bab7c752897ed340893e9e7bc915a138b645f45e83f2306237e6210af8669bf9:0d6a167fa5c74c07b848ed52f492496d','SRM','Féminin','Sandrine','Richard-Molard','1979-05-21 00:00:00',53,160,'enseignant','employee','PREREGISTERED',NULL,'0',14),(203,'tarkan.gezer@insa-lyon.fr','91e78ef784a1fc3dade2add929bb9602d064fc53fb7eece5fd7b3d1efb0dc377:bd98b8e11ff141f19966e1ab22f22386','Tarkg','Masculin','TARKAN','GEZER','1974-01-26 00:00:00',92,186,'enseignant','employee','PREREGISTERED',NULL,'0',15),(204,'chloe.lecheminant@insa-lyon.fr','4810858b68d05fbcce36c41b5e3fba756c70fc651f8db3b6f47f0ee6158fcf17:18101e6ea46f43f1983264b2e0992db0','Chloé','Féminin','chloe','LECHEMINANT','1990-01-08 00:00:00',50,160,'iatos','employee','PREREGISTERED',NULL,'0',38),(205,'anthony.faraut@insa-lyon.fr','644197838bf64ada165c69eca1427b8c41f8ac5b71efc0bf5f28c861489da7b4:338a5560087d4238b225d0454afc3754','Papalino','Masculin','Anthony','FARAUT','1991-06-26 00:00:00',72,180,'etudiant','student','PREREGISTERED',NULL,'0',3),(206,'laura.oxley@insa-lyon.fr','e9e66fe7abde358b0339f0b0090c3d2a316e251b9a9c94959cc5f0ceaa31440d:55f07d67876d45faa462d6bdc894eba9','Vive les escaliers ! ','Inconnu','','',NULL,NULL,NULL,'iatos','employee','PREREGISTERED',NULL,'0',39),(207,'mathieu.fabre@insa-lyon.fr','9d1b5baa846bbf8772dd5ba20a24261ce682cfd27c7ac04e8de5f4a8ab4faf9c:699d4930f2a849a2abba6b3685449947','Caramel','Inconnu','','',NULL,NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',4),(208,'suzanne.cawston@insa-lyon.fr','18ec255b7dff3f4be7fa040c1e56718767ded9d664699143cec557de02e3647c:44d909c6daf84184a28082f04f0eb04e','Suzanne Cawston','Féminin','Suzanne','Cawston','1983-05-10 00:00:00',57,168,'enseignant','employee','PREREGISTERED',NULL,'0',16),(209,'camille.delheure@insa-lyon.fr','ac1f4223bc7eb9f87ba0a435b325900997eaf4da061851f8e8bc6981d3fa43a0:d54001411c6540e2a2a6a445f17ba623','Camillou17','Féminin','Camille','Delheure','1993-06-28 00:00:00',60,168,'etudiant','student','PREREGISTERED',NULL,'0',5),(210,'clara.touzard@insa-lyon.fr','c730b1132e5bc252d58d6563f78504790eee3254d22056f9009bc40ad48a6ae0:2ac4f1faf11c45b790b966bc9a2aa980','Clarrypotter','Féminin','Clara','Touzard','1997-01-30 00:00:00',50,170,'etudiant','student','PREREGISTERED',NULL,'0',6),(211,'thomas.viola@insa-lyon.fr','245bebfe9125a432eeb076d5a2b1c60bdca240c6a1ad666234334794a2f4e48f:9866359648db416aa6abe6dbdb6bbb89','MP','Masculin','Thomas','VIOLA','1996-03-04 00:00:00',72,182,'etudiant','student','PREREGISTERED',NULL,'0',7),(212,'quentin.rouby@insa-lyon.fr','155081baf85a192096ef519adcc62db88f50577f4e194fca6313871d5d2b9f2e:1d861ffb2d3b48ac8b42c0924dbb72ad','PC','Masculin','Quentin','ROUBY','1996-09-24 00:00:00',63,167,'etudiant','student','PREREGISTERED',NULL,'0',8),(213,'berengere.guichon@insa-lyon.fr','1f46b8e2ce553ce39c87ea00c78dd8e3e8968992500c9d75c047d8cf13bc6035:63595adbd2dc4e9e9ac20eb1c23f2766','Bérengère','Féminin','','',NULL,NULL,NULL,'iatos','employee','PREREGISTERED',NULL,'0',40),(214,'florie.dessalle@insa-lyon.fr','205d63bf470d1f078aed21a2b6463a7e4fbd26e542da75213be3d95ae6c82451:7b6f139d3ac8401997f1cf816bef2d4e','Flo','Inconnu','','',NULL,NULL,NULL,'iatos','employee','PREREGISTERED',NULL,'0',41),(215,'charlelie.sellez@insa-lyon.fr','a12a1e1d0433219681cabb0a704539cc41cc22262a97ad8f03f977751e368e64:a26def40699740839bc42dd9f54bbc92','Charlé ','Masculin','Charlélie ','sellez','1992-03-31 00:00:00',70,169,'etudiant','student','PREREGISTERED',NULL,'0',9),(216,'farshid.dabaghi@insa-lyon.fr','5b10796246667ee14eeae61dac623845d1000d9a640a0a4646e54b822d07bec3:6dbc81c58843496799c41c238b8ded0f','Farshid','Inconnu','','',NULL,NULL,NULL,'enseignant','employee','PREREGISTERED',NULL,'0',17),(217,'andrea.pirrotta@insa-lyon.fr','88d422a645e059dc19ff95486d058b31c87868bb7efafbb253102a634303e7f1:19e689dbc4a5433fa774d071ee3388de','Andrea','Inconnu','','',NULL,NULL,NULL,'etudiant','student','PREREGISTERED',NULL,'0',10),(218,'mader@insa-lyon.fr','c9dc1615b8236fe2c8bc5afc47576ddbda65f9681e294c96e03012894a2ee672:22becb756a62462fa95668d1b0a0418d','bm','Masculin','Berthold','Mader','1955-08-19 00:00:00',70,169,'enseignant','employee','PREREGISTERED',NULL,'0',18),(219,'antton.tardio@insa-lyon.fr','1a2cd3c00cd9ba64f8d3dbf5e3ba9acfcbbf3467eac5c2eaecd04e4b5ab9f5f5:6489ce7140f7421fb599178eaa18d8c5','Ttun','Masculin','Antton','TARDIO','1994-11-08 00:00:00',70,174,'etudiant','student','PREREGISTERED',NULL,'0',11);
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person_steps`
--

DROP TABLE IF EXISTS `person_steps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `person_steps` (
  `person_id` int(11) DEFAULT NULL,
  `step_id` int(11) DEFAULT NULL,
  KEY `person_id` (`person_id`),
  KEY `step_id` (`step_id`),
  CONSTRAINT `person_steps_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`),
  CONSTRAINT `person_steps_ibfk_2` FOREIGN KEY (`step_id`) REFERENCES `steps` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person_steps`
--

LOCK TABLES `person_steps` WRITE;
/*!40000 ALTER TABLE `person_steps` DISABLE KEYS */;
/*!40000 ALTER TABLE `person_steps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `steps`
--

DROP TABLE IF EXISTS `steps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `steps` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `stepnumber` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `person_id` (`person_id`),
  CONSTRAINT `steps_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `steps`
--

LOCK TABLES `steps` WRITE;
/*!40000 ALTER TABLE `steps` DISABLE KEYS */;
/*!40000 ALTER TABLE `steps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `year` varchar(120) DEFAULT NULL,
  `cycle` varchar(120) DEFAULT NULL,
  `branch` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`id`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (7,'0','0','0'),(8,'0','0','0'),(10,'0','0','0'),(11,'0','0','0'),(13,'0','0','0'),(14,'0','0','0'),(29,'Quatrieme','Second','IF'),(30,'','',''),(34,'Quatrieme','Second','IF'),(35,'Quatrieme','Second','IF'),(36,'Quatrieme','Second','TC'),(37,'Quatrieme','Second','IF'),(48,'Quatrieme','Second','GE'),(49,'Troisieme','Second','GE'),(50,'Cinquieme','Second','IF'),(51,'Cinquieme','Second','TC'),(54,'','',''),(65,'Quatrieme','Second','GMD'),(70,'Troisieme','Second','GMD'),(71,'Cinquieme','Second','GMD'),(73,'Quatrieme','Second','BIM'),(80,'Quatrieme','Second','IF'),(81,'Quatrieme','Second','IF'),(82,'Troisieme','Second','GMPP'),(83,'Troisieme','Second','GMC'),(84,'Troisieme','Second','SGM'),(85,'Troisieme','Second','GMC'),(86,'Troisieme','Second','GMC'),(87,'Quatrieme','Second','GI'),(88,'Quatrieme','Second','IF'),(89,'','',''),(91,'Deuxieme','Premier',''),(93,'Deuxieme','Premier',''),(94,'','',''),(95,'Troisieme','Second','GE'),(96,'Premiere','Premier','Classique'),(98,'Premiere','Premier','Classique'),(100,'Premiere','Premier','Classique'),(101,'Deuxieme','Premier','Classique'),(110,'Troisieme','Second','GMPP'),(111,'Deuxieme','Premier','Internationale'),(112,'Premiere','Premier','Classique'),(115,'Troisieme','Second','GMPP'),(116,'Deuxieme','Premier','Internationale'),(120,'Deuxieme','Premier','Classique'),(121,'','',''),(124,'Cinquieme','Second','GMC'),(126,'Quatrieme','Second','GCU'),(127,'Quatrieme','Second','GCU'),(129,'Deuxieme','Premier','SHN'),(131,'Troisieme','Second','GI'),(132,'Deuxieme','Premier','SHN'),(137,'Premiere','Premier','Classique'),(138,'Premiere','Premier','Classique'),(143,'','',''),(148,'Deuxieme','Premier','Classique'),(149,'Deuxieme','Premier','Internationale'),(152,'Deuxieme','Premier','Classique'),(153,'Deuxieme','Premier','Classique'),(154,'Deuxieme','Premier','Classique'),(158,'Deuxieme','Premier','Classique'),(159,'','',''),(160,'Premiere','Premier','Internationale'),(161,'Premiere','Premier','Internationale'),(162,'Premiere','Premier','Classique'),(168,'Troisieme','Second','IF'),(170,'Troisieme','Second','GMC'),(171,'Quatrieme','Second','IF'),(173,'Premiere','Premier','Classique'),(174,'','',''),(175,'Quatrieme','Second','IF'),(176,'','',''),(177,'','',''),(178,'','',''),(179,'Premiere','Premier','Classique'),(188,'Premiere','Premier','Internationale'),(189,'Quatrieme','Second','SGM'),(190,'Quatrieme','Second','SGM'),(193,'Premiere','Premier','Classique'),(194,'Deuxieme','Premier','Classique'),(195,'Premiere','Premier','Classique'),(198,'','',''),(199,'','',''),(201,'Quatrieme','Second','IF'),(205,'Quatrieme','Second','IF'),(207,'','',''),(209,'Quatrieme','Second','GMC'),(210,'Premiere','Premier','Internationale'),(211,'Premiere','Premier','Internationale'),(212,'Premiere','Premier','Internationale'),(215,'Cinquieme','Second','GMD'),(217,'','',''),(219,'Troisieme','Second','GEN');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vip`
--

DROP TABLE IF EXISTS `vip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vip`
--

LOCK TABLES `vip` WRITE;
/*!40000 ALTER TABLE `vip` DISABLE KEYS */;
/*!40000 ALTER TABLE `vip` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-02-02 19:17:11
