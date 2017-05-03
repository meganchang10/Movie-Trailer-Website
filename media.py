import webbrowser

class Movie():
    """ This class provides a way to store movie related information """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # This initiates an instance of class movie with the following variables
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # This function plays the trailer when the box_image is clicked
    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
