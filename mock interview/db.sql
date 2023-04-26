/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - mock interview
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`mock interview` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `mock interview`;

/*Table structure for table `candidates` */

DROP TABLE IF EXISTS `candidates`;

CREATE TABLE `candidates` (
  `Can_id` int(11) NOT NULL AUTO_INCREMENT,
  `L_id` int(11) DEFAULT NULL,
  `F_name` varchar(20) DEFAULT NULL,
  `L_name` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `C_phone` int(10) DEFAULT NULL,
  `C_place` varchar(20) DEFAULT NULL,
  `C_pin` int(11) DEFAULT NULL,
  `C_post` int(11) DEFAULT NULL,
  KEY `Can_id` (`Can_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `candidates` */

insert  into `candidates`(`Can_id`,`L_id`,`F_name`,`L_name`,`email`,`C_phone`,`C_place`,`C_pin`,`C_post`) values 
(5,13,'nihala','sherin','nihala@gmail.com',2147483647,'kannur',0,0),
(6,14,'nihala','nihala','nihala@gmail.com',2147483647,'kannur',432234,0);

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `Cat_id` int(11) NOT NULL AUTO_INCREMENT,
  `L_id` int(11) DEFAULT NULL,
  `Category_name` varchar(20) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`Cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`Cat_id`,`L_id`,`Category_name`,`Date`) values 
(1,5,'df','2023-03-25'),
(2,5,'df','2023-03-25'),
(3,5,'dsdsf','2023-03-25'),
(4,5,'dsfdf','2023-03-25'),
(5,5,'science and technolo','2023-03-25'),
(6,5,'','2023-03-25'),
(7,2,'','2023-03-27'),
(8,17,'','2023-03-27'),
(9,15,'zz','2023-03-28'),
(10,17,'','2023-03-28'),
(11,17,'','2023-03-28'),
(12,17,'','2023-03-28'),
(13,17,'biology','2023-03-28'),
(14,17,'cccc','2023-03-28'),
(15,17,'','2023-03-28');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `C_id` int(10) NOT NULL,
  `L_id` int(11) DEFAULT NULL,
  `Complaint` varchar(10) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `reply` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`C_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`C_id`,`L_id`,`Complaint`,`Date`,`reply`) values 
(0,13,'bftghbn','2023-03-25','sorry');

/*Table structure for table `expert` */

DROP TABLE IF EXISTS `expert`;

CREATE TABLE `expert` (
  `E_id` int(10) NOT NULL AUTO_INCREMENT,
  `L__id` int(11) DEFAULT NULL,
  `first_name` varchar(10) DEFAULT NULL,
  `last_name` varchar(10) DEFAULT NULL,
  `Phone_no` bigint(10) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `post` varchar(30) DEFAULT NULL,
  `pin` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`E_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

/*Data for the table `expert` */

insert  into `expert`(`E_id`,`L__id`,`first_name`,`last_name`,`Phone_no`,`place`,`post`,`pin`,`email`) values 
(1,4,'Riya','jebin',2147483647,'kuttippuram','kuttippuram','786543','riya@gmail.com'),
(23,17,'paaru','abijith',467867579,'maniur','malap','654321','paru@gmail.com'),
(24,18,'','',0,'','','','');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `F_id` int(10) NOT NULL,
  `L_id` int(10) DEFAULT NULL,
  `feedback` varchar(10) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`F_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`F_id`,`L_id`,`feedback`,`Date`) values 
(1,13,'ffff','2023-03-25');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(10) DEFAULT NULL,
  `password` varchar(10) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`type`) values 
(4,'riya','riya','expert'),
(8,'','','candidate'),
(9,'','','candidates'),
(10,'','','candidates'),
(11,'','','candidates'),
(12,'','','candidates'),
(13,'','','candidate'),
(14,'nihala','nihala','candidate'),
(15,'admin','admin','admin'),
(17,'paru','paru','expert'),
(18,'','','expert');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `N_id` int(11) NOT NULL AUTO_INCREMENT,
  `Notification` varchar(10) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  KEY `N_id` (`N_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`N_id`,`Notification`,`Date`) values 
(2,NULL,NULL),
(4,'safana','2023-03-24'),
(5,'dfgfhj','2023-03-28');

/*Table structure for table `question` */

DROP TABLE IF EXISTS `question`;

CREATE TABLE `question` (
  `Q_id` int(11) NOT NULL AUTO_INCREMENT,
  `Questions` varchar(30) DEFAULT NULL,
  `T_id` int(11) DEFAULT NULL,
  `Answers` varchar(40) DEFAULT NULL,
  KEY `Q_id` (`Q_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `question` */

insert  into `question`(`Q_id`,`Questions`,`T_id`,`Answers`) values 
(2,'545665',0,'2'),
(4,'',0,'2'),
(5,'ssss',2,'sssss'),
(6,'',2,''),
(7,'z',2,'xcxv');

/*Table structure for table `result` */

DROP TABLE IF EXISTS `result`;

CREATE TABLE `result` (
  `R_id` int(11) NOT NULL,
  `L_id` int(11) DEFAULT NULL,
  `T_id` int(11) DEFAULT NULL,
  `Results` varchar(20) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`R_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `result` */

insert  into `result`(`R_id`,`L_id`,`T_id`,`Results`,`Date`) values 
(0,13,2,'hgfdss','2023-03-25'),
(1,1,1,'xcxvc','2023-03-28');

/*Table structure for table `test` */

DROP TABLE IF EXISTS `test`;

CREATE TABLE `test` (
  `T_id` int(11) NOT NULL AUTO_INCREMENT,
  `Test_name` varchar(20) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Cat_id` int(11) DEFAULT NULL,
  KEY `T_id` (`T_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `test` */

insert  into `test`(`T_id`,`Test_name`,`Date`,`Cat_id`) values 
(2,'csdfghygf','1970-01-04',1),
(3,'sss','2023-03-28',2);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
