#!/usr/bin/env python

import fresh_tomatoes

# `data` - list of lists of data with the following format
#    0: Title
#    1: Poster Image URL
#    2: Trailer YouTube URL
#    3: IMDB URL
#    4: List of leading actors
#

data = [
    [
        "The Godfather",
        "http://ia.media-imdb.com/images/M/MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@._V1_SX214_AL_.jpg",
        "http://www.youtube.com/watch?v=sY1S34973zA",
        "http://www.imdb.com/title/tt0068646/",
        ["Al Pacino", "Marlon Brando", "James Caan", "Diane Keaton"]
    ],
    [
        "The Godfather: Part II",
        "http://ia.media-imdb.com/images/M/MV5BNDc2NTM3MzU1Nl5BMl5BanBnXkFtZTcwMTA5Mzg3OA@@._V1_SX214_AL_.jpg",
        "https://www.youtube.com/watch?v=8PyZCU2vpi8",
        "http://www.imdb.com/title/tt0071562/?ref_=fn_al_tt_5",
        ["Al Pacino", "Robert DeNiro", "Robert Duvall", "Diane Keaton"]
    ],
    [
        "The Matrix",
        "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX214_AL_.jpg",
        "https://www.youtube.com/watch?v=m8e-FF8MsqU",
        "http://www.imdb.com/title/tt0133093/?ref_=fn_al_tt_1",
        ["Keanu Reaves", "Laurence Fishburn", "Carrie-Anne Moss"]
    ],
    [
        "Lucy",
        "http://ia.media-imdb.com/images/M/MV5BODcxMzY3ODY1NF5BMl5BanBnXkFtZTgwNzg1NDY4MTE@._V1_SX214_AL_.jpg",
        "https://www.youtube.com/watch?v=6Vu081NOorA",
        "http://www.imdb.com/title/tt2872732/?ref_=fn_al_tt_1",
        ["Scarlett Johansson", "Morgan Freeman", "Min-sik Choi"]
    ],
    [
        "Wreck-It Ralph",
        "http://ia.media-imdb.com/images/M/MV5BNzMxNTExOTkyMF5BMl5BanBnXkFtZTcwMzEyNDc0OA@@._V1_SX214_AL_.jpg",
        "https://www.youtube.com/watch?v=vf4r5q8-aWo",
        "http://www.imdb.com/title/tt1772341/?ref_=fn_al_tt_1",
        ["John C. Reilly", "Sarah Silverman", "Jack McBrayer", "Jane Lynch"]
    ]
]


class Movie:
    """A simple movie object with instance variables for
        - title
        - poster_image_url
        - trailer_youtube_url
        - imdb_url (The movie's imdb link)
        - actors (List of leading actors in the movie)
    """
    def __init__(self, title, poster_url, youtube_url, imdb_url, actors=[]):
        """Constructor"""
        # set the instance's instance variables
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_url
        self.imdb_url = imdb_url
        self.actors = actors

    def __str__(self):
        """Return a human-readable string of the Movie instance"""
        return "{0}: imdb: {1}, youtube: {2}, poster: {3}".format(
            self.title, self.imdb_url, self.trailer_youtube_url,
            self.poster_image_url)


def main():
    """Entry point for Full-Stack Nanodegree Project 1: Movie Trailer Website"""
    # list comprehensions rule!
    # This creates a list of Movie instances (we 'explode' each movie list in
    # `data` into Movie's constructor
    movies = [Movie(*movie) for movie in data]
    # generate the html and open a browser
    fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
    main()
