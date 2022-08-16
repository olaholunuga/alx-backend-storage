-- create user schema with
-- the includes an ENUM
DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users`
(
	`id` INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	`email` VARCHAR(255) NOT NULL UNIQUE,
	`name` VARCHAR(255) NOT NULL,
	`COUNTRY` ENUM('US', 'CO', 'TN') DEFAULT 'US'
);	
