-- Drop function if it already exists
DROP FUNCTION IF EXISTS SafeDiv;

-- Create SafeDiv function
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    -- Check if b is 0, return 0 if true, otherwise return a/b
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END //
DELIMITER ;
