/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 8.0.33 : Database - lifestyle
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`lifestyle` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `lifestyle`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add login',7,'add_login'),
(26,'Can change login',7,'change_login'),
(27,'Can delete login',7,'delete_login'),
(28,'Can view login',7,'view_login'),
(29,'Can add user',8,'add_user'),
(30,'Can change user',8,'change_user'),
(31,'Can delete user',8,'delete_user'),
(32,'Can view user',8,'view_user'),
(33,'Can add feedback',9,'add_feedback'),
(34,'Can change feedback',9,'change_feedback'),
(35,'Can delete feedback',9,'delete_feedback'),
(36,'Can view feedback',9,'view_feedback'),
(37,'Can add experts',10,'add_experts'),
(38,'Can change experts',10,'change_experts'),
(39,'Can delete experts',10,'delete_experts'),
(40,'Can view experts',10,'view_experts'),
(41,'Can add complaints',11,'add_complaints'),
(42,'Can change complaints',11,'change_complaints'),
(43,'Can delete complaints',11,'delete_complaints'),
(44,'Can view complaints',11,'view_complaints'),
(45,'Can add tutorial',12,'add_tutorial'),
(46,'Can change tutorial',12,'change_tutorial'),
(47,'Can delete tutorial',12,'delete_tutorial'),
(48,'Can view tutorial',12,'view_tutorial'),
(49,'Can add request',13,'add_request'),
(50,'Can change request',13,'change_request'),
(51,'Can delete request',13,'delete_request'),
(52,'Can view request',13,'view_request'),
(53,'Can add chat',14,'add_chat'),
(54,'Can change chat',14,'change_chat'),
(55,'Can delete chat',14,'delete_chat'),
(56,'Can view chat',14,'view_chat'),
(57,'Can add task',15,'add_task'),
(58,'Can change task',15,'change_task'),
(59,'Can delete task',15,'delete_task'),
(60,'Can view task',15,'view_task'),
(61,'Can add food',16,'add_food'),
(62,'Can change food',16,'change_food'),
(63,'Can delete food',16,'delete_food'),
(64,'Can view food',16,'view_food');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(14,'myapp','chat'),
(11,'myapp','complaints'),
(10,'myapp','experts'),
(9,'myapp','feedback'),
(16,'myapp','food'),
(7,'myapp','login'),
(13,'myapp','request'),
(15,'myapp','task'),
(12,'myapp','tutorial'),
(8,'myapp','user'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-06-01 05:36:56.604420'),
(2,'auth','0001_initial','2024-06-01 05:36:57.125979'),
(3,'admin','0001_initial','2024-06-01 05:36:57.296917'),
(4,'admin','0002_logentry_remove_auto_add','2024-06-01 05:36:57.300941'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-06-01 05:36:57.312952'),
(6,'contenttypes','0002_remove_content_type_name','2024-06-01 05:36:57.391924'),
(7,'auth','0002_alter_permission_name_max_length','2024-06-01 05:36:57.441242'),
(8,'auth','0003_alter_user_email_max_length','2024-06-01 05:36:57.471593'),
(9,'auth','0004_alter_user_username_opts','2024-06-01 05:36:57.487228'),
(10,'auth','0005_alter_user_last_login_null','2024-06-01 05:36:57.600773'),
(11,'auth','0006_require_contenttypes_0002','2024-06-01 05:36:57.608682'),
(12,'auth','0007_alter_validators_add_error_messages','2024-06-01 05:36:57.619251'),
(13,'auth','0008_alter_user_username_max_length','2024-06-01 05:36:57.678407'),
(14,'auth','0009_alter_user_last_name_max_length','2024-06-01 05:36:57.725817'),
(15,'auth','0010_alter_group_name_max_length','2024-06-01 05:36:57.755225'),
(16,'auth','0011_update_proxy_permissions','2024-06-01 05:36:57.755225'),
(17,'auth','0012_alter_user_first_name_max_length','2024-06-01 05:36:57.834823'),
(18,'myapp','0001_initial','2024-06-01 05:36:58.158401'),
(19,'myapp','0002_auto_20240530_1530','2024-06-01 05:36:58.801295'),
(20,'myapp','0003_alter_user_date','2024-06-01 05:36:58.867593'),
(21,'myapp','0004_experts_gender','2024-06-01 05:36:58.897099'),
(22,'myapp','0005_remove_experts_gender','2024-06-01 05:36:58.928954'),
(23,'myapp','0006_experts_gender','2024-06-01 05:36:58.966070'),
(24,'myapp','0007_tutorial_title','2024-06-01 05:36:58.976610'),
(25,'myapp','0008_task','2024-06-01 05:36:59.060834'),
(26,'myapp','0009_experts_date','2024-06-01 05:36:59.087850'),
(27,'myapp','0010_alter_experts_date','2024-06-01 05:36:59.165871'),
(28,'sessions','0001_initial','2024-06-01 05:36:59.213466'),
(29,'myapp','0011_food','2024-06-01 06:38:22.342057'),
(30,'myapp','0012_food_type','2024-06-01 06:41:09.128160'),
(31,'myapp','0013_auto_20240601_1242','2024-06-01 07:12:27.067991'),
(32,'myapp','0014_food_total','2024-06-01 09:09:46.261772'),
(33,'myapp','0015_remove_food_total','2024-06-01 09:14:42.103257'),
(34,'myapp','0016_auto_20240601_1503','2024-06-01 09:33:11.036654');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('163xnv5wt07mywqzlspchpgc6ttnmljl','.eJw9jDEKgDAUQ--SOUP9FYReRRxq_YLgIFpBEO9ulbZTEt4jN9ZlghPiPHT_i16b7hHOEkHgOmJOYYjVj3C9GGkHYvLRfytVrUCYqWbc8BNCFRoWyxY1lCcmmPTnBVjGJj0:1sF8fl:mMNMTReoVPPbhdIC0X3wKiady3Cclpr2PHWa_MmlVD8','2024-06-20 08:40:37.824424'),
('bvzip2dghaxe5claja612x5ftvelmk2y','eyJsaWQiOjJ9:1sF9BJ:-9UXwweJAndSvVbFxfep_LU2Lp-XWHKIeGV-yJn-3c4','2024-06-20 09:13:13.227762'),
('e62565dlhy8xfjmjmhcbe7pqkphcwpej','eyJsaWQiOjUsInRvdGFsX2NhbG9yaWVzX2J1cm5lZCI6MCwiY2Fsb3JpZV9nb2FsIjoyMDAwfQ:1sFQ7b:wqwalkxnMLyBsHTIkzQS-Lc99HxzEd-BnD0r1N_FjrM','2024-06-21 03:18:31.097049');

/*Table structure for table `myapp_chat` */

DROP TABLE IF EXISTS `myapp_chat`;

CREATE TABLE `myapp_chat` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `message` varchar(2000) NOT NULL,
  `FROMID_id` bigint NOT NULL,
  `TOID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_chat_FROMID_id_c34a39e8_fk_myapp_login_id` (`FROMID_id`),
  KEY `myapp_chat_TOID_id_c3a45261_fk_myapp_login_id` (`TOID_id`),
  CONSTRAINT `myapp_chat_FROMID_id_c34a39e8_fk_myapp_login_id` FOREIGN KEY (`FROMID_id`) REFERENCES `myapp_login` (`id`),
  CONSTRAINT `myapp_chat_TOID_id_c3a45261_fk_myapp_login_id` FOREIGN KEY (`TOID_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_chat` */

insert  into `myapp_chat`(`id`,`date`,`message`,`FROMID_id`,`TOID_id`) values 
(1,'2024-06-01','hi',3,5),
(2,'2024-06-01','hey',5,3);

/*Table structure for table `myapp_complaints` */

DROP TABLE IF EXISTS `myapp_complaints`;

CREATE TABLE `myapp_complaints` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaints` varchar(400) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `reply` varchar(400) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_complaints_USER_id_f1892848_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_complaints_USER_id_f1892848_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_complaints` */

insert  into `myapp_complaints`(`id`,`complaints`,`date`,`status`,`reply`,`USER_id`) values 
(1,'xcxcxfd','2021-06-01','pending','pending',1),
(2,'uiiyutry','2023-06-01','pending','pending',1),
(3,'uytuytuty','2023-06-01','pending','pending',1),
(4,'ffgfg','2021-06-01','pending','pending',1),
(5,'cgcfgfgf','2022-06-01','pending','pending',1),
(6,'tyuiuytr','2024-06-01','pending','pending',1),
(7,'ioiuy7t6r5e4rtyuj','2024-06-01','pending','pending',1);

/*Table structure for table `myapp_experts` */

DROP TABLE IF EXISTS `myapp_experts`;

CREATE TABLE `myapp_experts` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `idproof` varchar(500) NOT NULL,
  `image` varchar(500) NOT NULL,
  `type` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_experts_LOGIN_id_4d9c4268_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_experts_LOGIN_id_4d9c4268_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_experts` */

insert  into `myapp_experts`(`id`,`name`,`place`,`post`,`district`,`status`,`phone`,`email`,`LOGIN_id`,`idproof`,`image`,`type`,`gender`,`date`) values 
(1,'edvin ','hhhhhhh','kannur','ggggg','approved',9961207235,'edvin@gmail.com',3,'/media/1_IzBsbVj.jpg','/media/p5.png','Health_expert','','2022-06-01'),
(2,'thomas chacko','hhhhhhh','kannur','ggggg','pending',9961207232,'thomas@gmail.com',4,'/media/climate.jpg','/media/p7.png','Fitness_expert','','2024-06-01'),
(3,'thomas chacko','hhhhhhh','kannur','ggggg','pending',9961207231,'thomas@gmail.com',6,'/media/ab2.jpg','/media/c3.jpg','Health_expert','','2024-06-01');

/*Table structure for table `myapp_feedback` */

DROP TABLE IF EXISTS `myapp_feedback`;

CREATE TABLE `myapp_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_feedback_USER_id_fce7ccff_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_feedback_USER_id_fce7ccff_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_feedback` */

/*Table structure for table `myapp_food` */

DROP TABLE IF EXISTS `myapp_food`;

CREATE TABLE `myapp_food` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `USER_id` bigint NOT NULL,
  `type` varchar(500) NOT NULL,
  `callorie` int NOT NULL,
  `gram` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_food_USER_id_97876152_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_food_USER_id_97876152_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_food` */

insert  into `myapp_food`(`id`,`name`,`date`,`USER_id`,`type`,`callorie`,`gram`) values 
(3,'Apple','2024-06-03',1,'breakfast',104,200),
(4,'Peanuts','2024-06-01',1,'breakfast',567,100),
(5,'Chicken Biriyani','2024-06-02',1,'breakfast',3,2),
(6,'Ghee Rice','2024-06-02',1,'breakfast',100,100),
(7,'Rice','2024-06-01',1,'breakfast',224,200),
(8,'Alfaham','2024-06-01',1,'lunch',280,200),
(9,'Chicken Fry','2024-06-01',1,'lunch',300,120),
(10,'Rice','2024-06-01',1,'dinner',560,500),
(12,'Tandoori Chicken','2024-06-01',1,'lunch',400,200),
(13,'Ghee Rice','2024-06-01',1,'dinner',200,200),
(14,'Ghee Rice','2024-06-01',1,'breakfast',140,100),
(15,'Beef Fry','2024-06-01',1,'breakfast',602,200),
(16,'Rice','2024-06-01',1,'lunch',224,200),
(17,'Ghee Roast','2024-06-02',1,'breakfast',220,200),
(18,'Cofee','2024-05-31',2,'breakfast',0,50),
(19,'Dosa','2024-06-02',2,'breakfast',160,100),
(20,'Upma','2024-06-03',2,'breakfast',240,200),
(21,'Rice','2024-06-03',2,'lunch',280,250),
(22,'Biriyani','2024-06-03',2,'lunch',375,250),
(23,'Biriyani','2024-06-03',2,'dinner',375,250),
(24,'Banana','2024-06-03',2,'breakfast',356,400),
(25,'Rotti','2024-06-03',2,'breakfast',300,200),
(26,'Rotti','2024-06-06',1,'breakfast',300,200),
(27,'Rice','2024-06-06',2,'breakfast',224,200),
(28,'Puttu','2024-06-06',2,'breakfast',187,100);

/*Table structure for table `myapp_login` */

DROP TABLE IF EXISTS `myapp_login`;

CREATE TABLE `myapp_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`username`,`password`,`type`) values 
(1,'admin@gmail.com','admin','admin'),
(2,'sewag@gmail.com','12345678','user'),
(3,'sankardasnasd@gmail.com','12345678','expert'),
(4,'thomas1@gmail.com','12345678','pending'),
(5,'sachin@gmail.com','12345678','user'),
(6,'thomas@gmail.com','12345678','user');

/*Table structure for table `myapp_request` */

DROP TABLE IF EXISTS `myapp_request`;

CREATE TABLE `myapp_request` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `EXPERT_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_request_EXPERT_id_b040c3e5_fk_myapp_experts_id` (`EXPERT_id`),
  KEY `myapp_request_USER_id_8675c54c_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_request_EXPERT_id_b040c3e5_fk_myapp_experts_id` FOREIGN KEY (`EXPERT_id`) REFERENCES `myapp_experts` (`id`),
  CONSTRAINT `myapp_request_USER_id_8675c54c_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_request` */

insert  into `myapp_request`(`id`,`status`,`date`,`EXPERT_id`,`USER_id`) values 
(1,'accept','2024-06-01',1,2),
(2,'requested','2024-06-03',1,2);

/*Table structure for table `myapp_task` */

DROP TABLE IF EXISTS `myapp_task`;

CREATE TABLE `myapp_task` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(500) NOT NULL,
  `fromdate` date NOT NULL,
  `todate` date NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_task_USER_id_7d3176b7_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_task_USER_id_7d3176b7_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_task` */

insert  into `myapp_task`(`id`,`title`,`fromdate`,`todate`,`USER_id`) values 
(2,'erewrew','2024-06-06','2024-06-07',2),
(3,'reading books','2024-06-05','2024-06-14',1),
(4,'note read','2024-06-07','2024-06-21',1);

/*Table structure for table `myapp_tutorial` */

DROP TABLE IF EXISTS `myapp_tutorial`;

CREATE TABLE `myapp_tutorial` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `description` varchar(500) NOT NULL,
  `file` varchar(500) NOT NULL,
  `pdf` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `EXPERT_id` bigint NOT NULL,
  `title` varchar(500) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_tutorial_EXPERT_id_79c3e43d_fk_myapp_experts_id` (`EXPERT_id`),
  CONSTRAINT `myapp_tutorial_EXPERT_id_79c3e43d_fk_myapp_experts_id` FOREIGN KEY (`EXPERT_id`) REFERENCES `myapp_experts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_tutorial` */

/*Table structure for table `myapp_user` */

DROP TABLE IF EXISTS `myapp_user`;

CREATE TABLE `myapp_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `bmi` varchar(400) NOT NULL,
  `date` date NOT NULL,
  `height` varchar(100) NOT NULL,
  `image` varchar(400) NOT NULL,
  `weight` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_user_LOGIN_id_da832ded_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_user_LOGIN_id_da832ded_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_user` */

insert  into `myapp_user`(`id`,`name`,`place`,`post`,`district`,`email`,`phone`,`LOGIN_id`,`bmi`,`date`,`height`,`image`,`weight`) values 
(1,'sewag','cxzc','dgrff','adad','sewag@gmail.com','9961207235',2,'23.875114784205696','2024-06-01','165.0','/media/Screenshot%20(31).png','65.0'),
(2,'Sachin','cxzc','dgrff','adad','sachin@gmail.com','9961207238',5,'23.03','2024-06-01','168.0','/media/c1.jpg','65.0');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
