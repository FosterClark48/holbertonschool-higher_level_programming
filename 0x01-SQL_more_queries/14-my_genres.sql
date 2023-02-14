#!/usr/bin/python3
-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT name
    FROM tv_show_genres INNER JOIN tv_shows
    ON tv_show_genres.show_id = tv_shows.id
    JOIN tv_genres
    ON genre_id = tv_genres.id
    WHERE title = 'Dexter'
    ORDER BY name ASC;
