/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 10.4.28-MariaDB : Database - lifestyle
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`lifestyle` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `lifestyle`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
(25,'Can add experts',7,'add_experts'),
(26,'Can change experts',7,'change_experts'),
(27,'Can delete experts',7,'delete_experts'),
(28,'Can view experts',7,'view_experts'),
(29,'Can add login',8,'add_login'),
(30,'Can change login',8,'change_login'),
(31,'Can delete login',8,'delete_login'),
(32,'Can view login',8,'view_login'),
(33,'Can add task',9,'add_task'),
(34,'Can change task',9,'change_task'),
(35,'Can delete task',9,'delete_task'),
(36,'Can view task',9,'view_task'),
(37,'Can add user',10,'add_user'),
(38,'Can change user',10,'change_user'),
(39,'Can delete user',10,'delete_user'),
(40,'Can view user',10,'view_user'),
(41,'Can add tutorial',11,'add_tutorial'),
(42,'Can change tutorial',11,'change_tutorial'),
(43,'Can delete tutorial',11,'delete_tutorial'),
(44,'Can view tutorial',11,'view_tutorial'),
(45,'Can add task evaluation',12,'add_taskevaluation'),
(46,'Can change task evaluation',12,'change_taskevaluation'),
(47,'Can delete task evaluation',12,'delete_taskevaluation'),
(48,'Can view task evaluation',12,'view_taskevaluation'),
(49,'Can add request',13,'add_request'),
(50,'Can change request',13,'change_request'),
(51,'Can delete request',13,'delete_request'),
(52,'Can view request',13,'view_request'),
(53,'Can add food',14,'add_food'),
(54,'Can change food',14,'change_food'),
(55,'Can delete food',14,'delete_food'),
(56,'Can view food',14,'view_food'),
(57,'Can add feedback',15,'add_feedback'),
(58,'Can change feedback',15,'change_feedback'),
(59,'Can delete feedback',15,'delete_feedback'),
(60,'Can view feedback',15,'view_feedback'),
(61,'Can add exercises',16,'add_exercises'),
(62,'Can change exercises',16,'change_exercises'),
(63,'Can delete exercises',16,'delete_exercises'),
(64,'Can view exercises',16,'view_exercises'),
(65,'Can add event',17,'add_event'),
(66,'Can change event',17,'change_event'),
(67,'Can delete event',17,'delete_event'),
(68,'Can view event',17,'view_event'),
(69,'Can add emotion',18,'add_emotion'),
(70,'Can change emotion',18,'change_emotion'),
(71,'Can delete emotion',18,'delete_emotion'),
(72,'Can view emotion',18,'view_emotion'),
(73,'Can add complaints',19,'add_complaints'),
(74,'Can change complaints',19,'change_complaints'),
(75,'Can delete complaints',19,'delete_complaints'),
(76,'Can view complaints',19,'view_complaints'),
(77,'Can add chat',20,'add_chat'),
(78,'Can change chat',20,'change_chat'),
(79,'Can delete chat',20,'delete_chat'),
(80,'Can view chat',20,'view_chat');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(20,'myapp','chat'),
(19,'myapp','complaints'),
(18,'myapp','emotion'),
(17,'myapp','event'),
(16,'myapp','exercises'),
(7,'myapp','experts'),
(15,'myapp','feedback'),
(14,'myapp','food'),
(8,'myapp','login'),
(13,'myapp','request'),
(9,'myapp','task'),
(12,'myapp','taskevaluation'),
(11,'myapp','tutorial'),
(10,'myapp','user'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-06-18 05:20:05.045086'),
(2,'auth','0001_initial','2024-06-18 05:20:05.588708'),
(3,'admin','0001_initial','2024-06-18 05:20:05.715787'),
(4,'admin','0002_logentry_remove_auto_add','2024-06-18 05:20:05.727686'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-06-18 05:20:05.742287'),
(6,'contenttypes','0002_remove_content_type_name','2024-06-18 05:20:05.804720'),
(7,'auth','0002_alter_permission_name_max_length','2024-06-18 05:20:05.918249'),
(8,'auth','0003_alter_user_email_max_length','2024-06-18 05:20:05.930830'),
(9,'auth','0004_alter_user_username_opts','2024-06-18 05:20:05.946457'),
(10,'auth','0005_alter_user_last_login_null','2024-06-18 05:20:06.010875'),
(11,'auth','0006_require_contenttypes_0002','2024-06-18 05:20:06.014614'),
(12,'auth','0007_alter_validators_add_error_messages','2024-06-18 05:20:06.025712'),
(13,'auth','0008_alter_user_username_max_length','2024-06-18 05:20:06.041805'),
(14,'auth','0009_alter_user_last_name_max_length','2024-06-18 05:20:06.057818'),
(15,'auth','0010_alter_group_name_max_length','2024-06-18 05:20:06.074007'),
(16,'auth','0011_update_proxy_permissions','2024-06-18 05:20:06.089132'),
(17,'auth','0012_alter_user_first_name_max_length','2024-06-18 05:20:06.104948'),
(18,'myapp','0001_initial','2024-06-18 05:20:07.281227'),
(19,'sessions','0001_initial','2024-06-18 05:20:07.340781');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('0uwcwa9n7c0lj6gmqod7mu4hqlq42eh7','.eJxVTksKgzAQvcusgybxU3XXc5QiMY5iiUZibAuld--oBXVW7zu8D5iuhkIy0DMUIs_SICLsduytV6bUyljX4VRWsxuQGoJzym1q2VplSMoWrRFQwNUY-6IYUUkGg6cyYv9JbJGj4MIPFycM5gndWsD3iM5vyyhLj42qoLhJLuM7g1p5RUwQxJOBf0cS1idHHzrNQCPDHutOhYvNU56XIpZJlAaPsaXdvl9njEhJ_v0BPhZQcw:1sJTgd:UDhYwJpD98PF1qmxpp2LT0bPmjq17G1N-JQ3TlV9XKI','2024-07-02 07:55:27.038330'),
('n5j8hgwa6lwaxrqtmx0ie0u24vvui4zg','.eJyrVsrJTFGyMtJRSi5VsjK0tDDTMwayi4BsCwi7JL8kMSc-OTEnvygztTg-qbQoLxWow9DAAKgOIhqfnp-YA9IBEkszVLJScs7PKy7NBaoD8o2A_KDU3MTMvMy8dKBAWWKOIVQ_kGkEs6kWAC0TKIA:1sJTFW:xmsSxbMqgZkM8DboMPM7awP7Na_lyYi68bW6I2gxqe0','2024-07-02 07:27:26.692211'),
('od1iznl4izl8sletx1rxm9va9c8zffyr','.eJw1jUEOwjAMBP_ic4XqgGiba3_AByJT0iqSm0hpwgXxdzYgbrOrWftFGh5kTUdLJcvTeD2dwRk8DpfGJRVRt4imHPzh7jVHj0UP69e5LYk2v0dX2jXuaGWyNKd41B02skG--V1CDHFD8RSFwmy-aP7_3h8uhyo4:1sJROU:oPzsBF9zYaJhw5quTYJRyHamKB8YUKaB0L85X94cjgI','2024-07-02 05:28:34.649299');

/*Table structure for table `myapp_chat` */

DROP TABLE IF EXISTS `myapp_chat`;

CREATE TABLE `myapp_chat` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `message` varchar(2000) NOT NULL,
  `FROMID_id` bigint(20) NOT NULL,
  `TOID_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_chat_FROMID_id_c34a39e8_fk_myapp_login_id` (`FROMID_id`),
  KEY `myapp_chat_TOID_id_c3a45261_fk_myapp_login_id` (`TOID_id`),
  CONSTRAINT `myapp_chat_FROMID_id_c34a39e8_fk_myapp_login_id` FOREIGN KEY (`FROMID_id`) REFERENCES `myapp_login` (`id`),
  CONSTRAINT `myapp_chat_TOID_id_c3a45261_fk_myapp_login_id` FOREIGN KEY (`TOID_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_chat` */

insert  into `myapp_chat`(`id`,`date`,`message`,`FROMID_id`,`TOID_id`) values 
(1,'2024-06-18','hi how cani help u',3,2),
(2,'2024-06-18','i am feeling bad',2,3),
(3,'2024-06-18','kuhsius',3,2),
(4,'2024-06-18','dskhfuskfhk',2,3);

/*Table structure for table `myapp_complaints` */

DROP TABLE IF EXISTS `myapp_complaints`;

CREATE TABLE `myapp_complaints` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `complaints` varchar(400) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `reply` varchar(400) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_complaints_USER_id_f1892848_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_complaints_USER_id_f1892848_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_complaints` */

insert  into `myapp_complaints`(`id`,`complaints`,`date`,`status`,`reply`,`USER_id`) values 
(1,'very bad','2024-06-18','replied','its k i will manage',1);

/*Table structure for table `myapp_emotion` */

DROP TABLE IF EXISTS `myapp_emotion`;

CREATE TABLE `myapp_emotion` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `happy` double NOT NULL,
  `stress` double NOT NULL,
  `date` date NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_emotion_USER_id_c1178571_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_emotion_USER_id_c1178571_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_emotion` */

insert  into `myapp_emotion`(`id`,`happy`,`stress`,`date`,`USER_id`) values 
(1,75,25,'2024-06-18',1),
(2,45,55,'2024-06-18',1),
(3,75,25,'2024-06-18',1),
(4,75,25,'2024-06-18',1),
(5,75,25,'2024-06-18',1),
(6,75,25,'2024-06-18',1),
(7,20,80,'2024-06-18',1),
(8,20,80,'2024-06-18',1),
(9,20,80,'2024-06-18',1),
(10,20,80,'2024-06-18',1);

/*Table structure for table `myapp_event` */

DROP TABLE IF EXISTS `myapp_event`;

CREATE TABLE `myapp_event` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `event` varchar(500) NOT NULL,
  `status` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `rdate` date NOT NULL,
  `rtime` time(6) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_event_USER_id_33f3d6ee_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_event_USER_id_33f3d6ee_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_event` */

insert  into `myapp_event`(`id`,`event`,`status`,`date`,`time`,`rdate`,`rtime`,`USER_id`) values 
(1,'cousin\'s bday','viewed','2024-07-10','17:00:00.000000','2024-06-18','10:57:00.000000',1);

/*Table structure for table `myapp_exercises` */

DROP TABLE IF EXISTS `myapp_exercises`;

CREATE TABLE `myapp_exercises` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `time` double NOT NULL,
  `type` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `callorie` int(11) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_exercises_USER_id_2976b7f4_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_exercises_USER_id_2976b7f4_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_exercises` */

insert  into `myapp_exercises`(`id`,`time`,`type`,`date`,`callorie`,`USER_id`) values 
(1,2,'Yoga','2024-06-17',300,1),
(2,2,'Cycling','2024-06-18',720,1);

/*Table structure for table `myapp_experts` */

DROP TABLE IF EXISTS `myapp_experts`;

CREATE TABLE `myapp_experts` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(500) NOT NULL,
  `idproof` varchar(500) NOT NULL,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `gender` varchar(100) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_experts_LOGIN_id_4d9c4268_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_experts_LOGIN_id_4d9c4268_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_experts` */

insert  into `myapp_experts`(`id`,`image`,`idproof`,`name`,`place`,`post`,`district`,`phone`,`email`,`type`,`status`,`date`,`gender`,`LOGIN_id`) values 
(1,'/media/20240609_142536.jpg','/media/20240609_131700.jpg','Goutham','kochi','udl','ernakulam',9845637289,'goutham@gmail.com','Fitness_expert','approved','2024-06-18','',3),
(2,'/media/20240609_131700_bUuKTIE.jpg','/media/20240609_131712.jpg','adhithya','kochi','udl','ernakulam',9845637289,'adhithya@gmail.com','Health_expert','pending','2024-06-18','',4);

/*Table structure for table `myapp_feedback` */

DROP TABLE IF EXISTS `myapp_feedback`;

CREATE TABLE `myapp_feedback` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_feedback_USER_id_fce7ccff_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_feedback_USER_id_fce7ccff_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_feedback` */

insert  into `myapp_feedback`(`id`,`feedback`,`date`,`USER_id`) values 
(1,'good','2024-06-18',1);

/*Table structure for table `myapp_food` */

DROP TABLE IF EXISTS `myapp_food`;

CREATE TABLE `myapp_food` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `type` varchar(500) NOT NULL,
  `name` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `gram` int(11) NOT NULL,
  `callorie` int(11) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_food_USER_id_97876152_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_food_USER_id_97876152_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_food` */

insert  into `myapp_food`(`id`,`type`,`name`,`date`,`gram`,`callorie`,`USER_id`) values 
(1,'breakfast','Rice','2024-06-17',100,112,1),
(2,'dinner','Ghee rice','2024-06-18',250,100,1);

/*Table structure for table `myapp_login` */

DROP TABLE IF EXISTS `myapp_login`;

CREATE TABLE `myapp_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`username`,`password`,`type`) values 
(1,'admin@gmail.com','admin','admin'),
(2,'nazrin@gmail.com','nazrin','user'),
(3,'goutham@gmail.com','goutham','expert'),
(4,'adhithya@gmail.com','adhithya','pending');

/*Table structure for table `myapp_request` */

DROP TABLE IF EXISTS `myapp_request`;

CREATE TABLE `myapp_request` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `EXPERT_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_request_EXPERT_id_b040c3e5_fk_myapp_experts_id` (`EXPERT_id`),
  KEY `myapp_request_USER_id_8675c54c_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_request_EXPERT_id_b040c3e5_fk_myapp_experts_id` FOREIGN KEY (`EXPERT_id`) REFERENCES `myapp_experts` (`id`),
  CONSTRAINT `myapp_request_USER_id_8675c54c_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_request` */

insert  into `myapp_request`(`id`,`status`,`date`,`EXPERT_id`,`USER_id`) values 
(1,'accept','2024-06-18',1,1);

/*Table structure for table `myapp_task` */

DROP TABLE IF EXISTS `myapp_task`;

CREATE TABLE `myapp_task` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(500) NOT NULL,
  `fromdate` date NOT NULL,
  `todate` date NOT NULL,
  `Duration` int(11) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_task_USER_id_7d3176b7_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_task_USER_id_7d3176b7_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_task` */

/*Table structure for table `myapp_taskevaluation` */

DROP TABLE IF EXISTS `myapp_taskevaluation`;

CREATE TABLE `myapp_taskevaluation` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `score` int(11) NOT NULL,
  `TASK_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_taskevaluation_TASK_id_8a2ffbbf_fk_myapp_task_id` (`TASK_id`),
  CONSTRAINT `myapp_taskevaluation_TASK_id_8a2ffbbf_fk_myapp_task_id` FOREIGN KEY (`TASK_id`) REFERENCES `myapp_task` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_taskevaluation` */

/*Table structure for table `myapp_tutorial` */

DROP TABLE IF EXISTS `myapp_tutorial`;

CREATE TABLE `myapp_tutorial` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(500) NOT NULL,
  `file` varchar(500) NOT NULL,
  `pdf` varchar(500) NOT NULL,
  `title` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `EXPERT_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_tutorial_EXPERT_id_79c3e43d_fk_myapp_experts_id` (`EXPERT_id`),
  CONSTRAINT `myapp_tutorial_EXPERT_id_79c3e43d_fk_myapp_experts_id` FOREIGN KEY (`EXPERT_id`) REFERENCES `myapp_experts` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_tutorial` */

insert  into `myapp_tutorial`(`id`,`description`,`file`,`pdf`,`title`,`date`,`EXPERT_id`) values 
(1,'new workout routine','/media/2024-06-18-12-54-51.mp4','/media/2024-06-18-12-54-52.pdf','zumba','2024-06-18',1);

/*Table structure for table `myapp_user` */

DROP TABLE IF EXISTS `myapp_user`;

CREATE TABLE `myapp_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `dob` varchar(30) NOT NULL,
  `height` varchar(100) NOT NULL,
  `weight` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `image` varchar(400) NOT NULL,
  `bmi` varchar(400) NOT NULL,
  `date` date NOT NULL,
  `calorie` double NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_user_LOGIN_id_da832ded_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_user_LOGIN_id_da832ded_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_user` */

insert  into `myapp_user`(`id`,`name`,`place`,`gender`,`dob`,`height`,`weight`,`post`,`district`,`email`,`phone`,`image`,`bmi`,`date`,`calorie`,`LOGIN_id`) values 
(1,'Nazrin','kochi','Female','2001-03-08','153.0','60.0','udl','ernakulam','nazrin@gmail.com','7306179856','/media/20240609_142517.jpg','25.63','2024-06-18',1986.3,2);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
