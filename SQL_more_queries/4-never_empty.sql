-- 4. ID can't be null
CREATE TABLE IF NOT EXISTS id_not_null (
	id INTEGER DEFAULT 1,
	name VARCHAR(256)
)