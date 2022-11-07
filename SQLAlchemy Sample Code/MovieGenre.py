from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base
# cannot import 'Movie' from partially initialized module 'Movie'
# from Movie import Movie
# cannot import 'Genre' from partially initialized module 'Genre'
# from Genre import Genre
"""I would very much preferred to have imported Movie and Genre so that I could reference
them as types in the code below.  But because those two classes MUST reference this one,
there is no way to do that without setting up a cyclic import relationship.  You would not
have this sort of problem with Java since it's a compiled langauge.  But Python being an
interpreted language creates a bit of a problem for us here."""


class MovieGenre(Base):
    __tablename__ = 'movies_genres'
    movie_id = Column(Integer, ForeignKey('movies.movies_id'), primary_key=True, nullable=False)
    genre_name = Column(String(16), ForeignKey('genres.name'), primary_key=True, nullable=False)
    """This is a bi-directional relationship between MovieGenre and Movie.  The variable in Movie
    that keeps track of the instances of MovieGenres is called genres_list."""
    movie = relationship("Movie", back_populates='genres_list')
    # movies_list is the name of the list of MovieGenre instances for the parent movie.
    genre = relationship("Genre", back_populates='movies_list')

    """Create an instance of the junction table.
    @param      movie       The movie that belongs to the given genre.
    @param      genre       The genre that the movie belongs to."""
    def __init__(self, movie, genre):
        # This is more for the database than anything else.  This is what gets stored to disk.
        self.movie_id = movie.movies_id
        # Same thing here.
        self.genre_name = genre.name
        # These next two properties are strictly from the OO perspective.
        self.movie = movie
        self.genre = genre
