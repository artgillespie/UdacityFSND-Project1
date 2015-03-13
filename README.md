# Project 1 : Movie Trailers Website

## Running the application
1. Ensure you have python installed
2. At a terminal/cmd prompt, type `python project_1.py` to generate the movie
   trailer page and open it in your default browser.

## Customizing the application
You can add more movies to the trailer website by adding them to the `data` list
at the top of `project_1.py`. The format of the list is as follows:

* 0: Title
* 1: Poster Image URL
* 2: Trailer YouTube URL
* 3: IMDB URL
* 4: (Optional) List of leading actors

## NOTES
Modified the following in the Udacity-supplied `fresh_tomatoes.py`:

1. Changed `movie_tile_content` to support additional fields (namely `imdb_url`
   and `movie_title`). When I made the movie title `<h2>` a link to imdb, I
noticed a bug where clicking on the link would briefly open the youtube modal
before loading the imdb page. After some debugging, I deterimined that this was
because we were adding a click listener to any element with the `.movie-tile`
class. Since the link was inside the `.movie-tile` div, that click listener was
intercepting the click on the link and opening the modal.  I changed the
listener to listen for clicks on the new `.movie-poster` class and enclosed the
poster image in a div with this class. Fixed!

2. There was a bug in the generated html related to Bootstrap: The movie tiles
   have Bootstrap column classes (`col-md-6` and `col-lg-4`) but were not
enclosed in a block element with the `row` class. This prevented the tiles from
being laid out correctly when spanning multiple rows and from re-flowing
correctly when the browser window is resized. I enclosed the tiles in `<div
class="row">...</div>` which fixed the layout.
