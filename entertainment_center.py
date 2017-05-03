import media
import fresh_tomatoes

""" Create an object of type movie using the media.Movie class. For neatness,
    I assign values to each variable (title, storyline, poster_image,
    trailer_youtube), then pass the variables through to the class to create
    the instance."""

title = "Mulan"
storyline = ("The story of a man falling in love with another man only to "
            + "discover the man is actually a girl!")
poster_image = "http://www.reocities.com/Hollywood/5082/sword.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=ZSS5dEeMX64"
mulan = media.Movie(title, storyline, poster_image, trailer_youtube)

title = "Cabin in the Woods"
storyline = "The most epic of horror films spoofs"
poster_image = "https://i.jeded.com/i/the-cabin-in-the-woods.31227.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=uWX_RPnUpBk"
cabin_in_the_woods = media.Movie(title,storyline,poster_image, trailer_youtube)

title = "Silver Linings Playbook"
storyline = ("Jennifer Lawrence and Bradley Cooper try to outcrazy each other "
             + "in this quirky dramedy.")
poster_image = "http://www.impawards.com/2012/posters/silver_linings_playbook.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=Lj5_FhLaaQQ"
silver_linings_playbook = media.Movie(title,storyline,poster_image,
                          trailer_youtube)

title = "Good Will Hunting"
storyline = ("Matt Damon is a janitor who is secretly smart." +
            " Robin Williams tells fart jokes.")
poster_image = "http://www.impawards.com/1997/posters/good_will_hunting.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=PaZVjZEFkRs"
good_will_hunting = media.Movie(title,storyline,poster_image, trailer_youtube)

title = "La La Land"
storyline = "Old school musical style set in a modern world"
poster_image = "https://d35fkdjhhgt99.cloudfront.net/static/use-media-items/48/47382/full-1382x2048/587a5198/1.jpeg?resolution=0"
trailer_youtube = "https://www.youtube.com/watch?v=0pdqf4P9MB8"
la_la_land = media.Movie(title,storyline,poster_image, trailer_youtube)

title = "Get Out"
storyline = "White people try to become black people"
poster_image = "https://cdn.traileraddict.com/content/universal-pictures/get-out-2017-2.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=xnkgiINreIk"
get_out = media.Movie(title,storyline,poster_image, trailer_youtube)

""" Here, we create a list of all the movies. We pass this list through to the
    open_movies_page function in the fresh_tomatoes module to create the
    webpage and open it."""
movies = [mulan, cabin_in_the_woods, silver_linings_playbook,
          good_will_hunting, la_la_land, get_out]
fresh_tomatoes.open_movies_page(movies)
