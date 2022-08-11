-- create trigger for update event
DELIMITER $$
CREATE TRIGGER `email_valid`
BEFORE UPDATE ON `users`
FOR EACH ROW
BEGIN
IF NEW.email != OLD.email
THEN
SET NEW.valid_email = 0;
END IF;
END;
$$
