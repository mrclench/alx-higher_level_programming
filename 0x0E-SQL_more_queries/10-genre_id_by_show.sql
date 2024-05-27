-- Import database dump from hbtn_0d_tvshows
-- list all shows in database wth at least 1 genre linked 
-- ASC order by tv_shows.title and tv_show_genres.genre_id
-- use SELECT once
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id=tv_show_genres.genre_id
ORDER BY tv_shows.title;
