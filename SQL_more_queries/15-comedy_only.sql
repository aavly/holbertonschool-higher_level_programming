-- 15. Only Comedy
SELECT t.title
FROM tv_shows t
JOIN tv_show_genres tsg ON t.id = tsg.show_id
JOIN tv_genres tg ON tsg.genre_id = tg.id
WHERE tg.name = 'Comedy'
ORDER BY t.title