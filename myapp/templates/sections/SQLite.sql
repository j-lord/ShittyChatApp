-- classify every message as client message True/False
-- UPDATE history
--     SET is_Client_Message = (
--         SELECT is_Client 
--         FROM user
--         WHERE username = history.user);

-- UPDATE history
--     SET is_Client_Message = NULL WHERE id > 0;

-- Reverse list order
-- SELECT id   
-- FROM history
-- ORDER BY id DESC;

-- Clear out all messages 
    -- DELETE FROM history
    -- WHERE id > 0;
    -- SELECT * from user;

-- UPDATE user SET is_Client = "False" WHERE id = 1;
-- SELECT username FROM user WHERE is_Client = "True";

-- SELECT * from user;

-- UPDATE history
-- SET user = "John"
-- WHERE id = 4;

-- WHERE id = 1; 

-- ALTER TABLE history
-- -- RENAME COLUMN is_Clinet_Message TO is_Client_Message;
-- ADD COLUMN is_Client_Message;

-- ALTER TABLE user
-- RENAME COLUMN is_Clinet_Message TO is_Client_Message;
-- ADD COLUMN is_Client;

-- SELECT * from user;

SELECT * from history;
-- ADD COLUMN is_Clinet boolean