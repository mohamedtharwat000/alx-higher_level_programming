/*
script that lists all shows,
and all genres linked to that show,
from the database hbtn_0d_tvshows.
*/

-- lists all shows, and all genres linked to that showw
    SELECT tv_shows.title AS `title`, tv_genres.name AS `genre`
      FROM tv_shows
 LEFT JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
 LEFT JOIN tv_genres
        ON tv_genres.id = tv_show_genres.genre_id
     UNION
    SELECT tv_shows.title AS `title`, tv_genres.name AS `genre`
      FROM tv_shows
RIGHT JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
RIGHT JOIN tv_genres
        ON tv_genres.id = tv_show_genres.genre_id
  ORDER BY `title`, `genre` ASC;
