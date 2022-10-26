DROP TABLE IF EXISTS `employees`;
CREATE TABLE `employees` (
	`employee_id` int NOT NULL AUTO_INCREMENT,
	`email` char(50) NOT NULL,
	`password` char(60) NOT NULL,
	`fullname` char(50) NOT NULL,
	`salary` int NOT NULL,
	`isHR` BOOLEAN NOT NULL,
	PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

LOCK TABLES `employees` WRITE;
INSERT INTO employees VALUES (NULL, 'admin@imployee.id', '$2b$12$HJie5kftgDhSgIbuYklckeG1YvZuCppb1Jjcu2nPcSaRuPqW3aeLq', 'Alvina Maharni', '12000000', 1);
UNLOCK TABLES;