CREATE DATABASE IF NOT EXISTS `imployee` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `imployee`;

CREATE TABLE IF NOT EXISTS `employees` (
	`employee_id` int NOT NULL AUTO_INCREMENT,
	`email` char(50) NOT NULL,
	`password` char(50) NOT NULL,
	`fullname` char(50) NOT NULL,
	`salary` int NOT NULL,
	`isHR` BOOLEAN NOT NULL,
	PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

INSERT INTO employees VALUES (NULL, 'admin@imployee.id', '$2b$12$HJie5kftgDhSgIbuYklckeG1YvZuCppb1Jjcu2nPcSaRuPqW3aeLq', 'Alvina Maharni', '12000000', 1);