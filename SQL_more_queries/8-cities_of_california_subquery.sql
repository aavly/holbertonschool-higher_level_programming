-- 8. Cities of California
SELECT id, name FROM cities
WHERE state_id = (
	SELECT id FROM States
	WHERE name = 'California'
)
ORDER BY id;