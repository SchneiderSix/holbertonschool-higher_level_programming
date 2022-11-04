-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT name FROM tv_genres JOIN tv_show_genres ON title = "Dexter";