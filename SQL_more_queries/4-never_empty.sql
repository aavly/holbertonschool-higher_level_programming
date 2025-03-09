-- 4. ID can't be null
-- Write a script that creates the table id_not_null of your MySQL server
CREATE TABLE IF NOT EXISTS id_not_null (
	id INTEGER DEFAULT 1,
	name VARCHAR(256)
)