#!/usr/bin/python3
-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT title, name
    FROM tv_shows LEFT OUTER JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
    LEFT OUTER JOIN tv_genres
    ON genre_id = tv_genres.id
    ORDER BY title, name ASC;
