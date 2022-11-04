-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT name FROM tv_genres JOIN tv_show_genres ON id = tv_show_genres.show_id WHERE title = Dexter;