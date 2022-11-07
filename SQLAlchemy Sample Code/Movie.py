from sqlalchemy import Column, Integer, Identity, Float, \
    String, UniqueConstraint
from sqlalchemy.orm import relationship

from orm_base import Base
from MovieGenre import MovieGenre
# Trying to resolve circular imports.
# from Genre import Genre


class Movie(Base):
    __tablename__ = "movies"
    movies_id = Column('movies_id', Integer, Identity(start=1, cycle=True),
                       nullable=False, primary_key=True)
    name = Column('name', String(100), nullable=False)
    year_released = Column('year_released', Integer, nullable=False)
    movie_rank = Column('movie_rank', Float, nullable=True)
    # In general, table_args allows you to directly influence the DDL.  In this case, to
    # include a candidate key.
    table_args = (UniqueConstraint('name', 'year_released', name='movies_uk_01'),)
    """This is a bi-directional relationship from Movie to MovieGenre.  Every relationship
    really has two perspectives: the OO and the database.  Because this relationship is
    bi-directional, we need to let SQLAlchemy know how to keep each end in sync with the other.
    back_populates is the name of the scalar in MovieGenre that is a reference to this instance 
    of Movie.  genres_list is how the movie keeps track of the genres it belongs to."""
    genres_list: [MovieGenre] = relationship("MovieGenre", back_populates="movie", viewonly=False)

    def __init__(self, name: String, year_released: Integer, movie_rank: Float):
        self.name = name
        self.year_released = year_released
        self.movie_rank = movie_rank
        self.genres_list = []

    """Add a genre to the list of genres that apply to this movie.
    @param      genre       The instance of genre that applies to this movie."""
    def add_genre(self, genre):
        # make sure this genre is non already on the list.
        for next_genre in self.genres_list:
            if next_genre == genre:
                return
        # Create an instance of the junction table class for this relationship.
        movie_genre = MovieGenre(self, genre)
        # Update this move to reflect that we have this genre now.
        genre.movies_list.append(movie_genre)
        # Update the genre to reflect this movie.
        self.genres_list.append(movie_genre)
