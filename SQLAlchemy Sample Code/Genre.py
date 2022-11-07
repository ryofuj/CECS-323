from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from orm_base import Base
from MovieGenre import MovieGenre
# I'm trying to avoid a circular import by removing Movie from the mix.
# from Movie import Movie


class Genre(Base):
    __tablename__ = "genres"
    name = Column("name", String(16), nullable=False, primary_key=True)
    """movies_list is how the genre keeps track of the movies that it characterizes.
    back_populates tells SQLAlchemy to keep movies_list in this class in sync with 
    the genre scalar attribute in the movies_genres instances associated with this 
    genre."""
    movies_list: [MovieGenre] = relationship("MovieGenre", back_populates="genre", viewonly=False)

    def __init__(self, name: String):
        self.name = name
        # I believe that this also allocates space in RAM for the list of MoveGenre instances.
        self.movies_list = []

    """Add a movie to the list of movies that are characterized by this genre.
    @param      movie       The movie instance to add.  I cannot import the Movie class in 
                            this class because that creates a cyclic import.  So I'm not able 
                            to indicate that this argument be of type Movie."""
    def add_movie(self, movie):
        for next_movie in self.movies_list:
            if next_movie == movie:
                return
        # Create an instance of the junction table class.
        movie_genre = MovieGenre(movie, self)
        # add that new instance to the list of genres that the Movie keeps.
        movie.genres_list.append(movie_genre)
        # add that new instance to the list of movies that this genre keeps.
        self.movies_list.append(movie_genre)

    def __str__(self):
        return "Genre: {genre_name}".format(genre_name = self.name)
