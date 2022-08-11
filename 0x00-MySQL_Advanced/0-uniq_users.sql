-- create table users
-- attributes: name, email, id
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`
(
	`id` INT AUTO_INCREMENT NOT NULL,
	`email` VARCHAR(255) NOT NULL UNIQUE,
	`name` VARCHAR(255),
	PRIMARY KEY (`id`)
);
