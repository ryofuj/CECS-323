"""This "application" is a demonstration using SQLAlchemy to create a small number of tables and populate
them.  Not evey possible use case for SQLAlchemy is explored in this demonstration, only those which are
required for this particular demonstration.

Technical Note: Be sure to have psycopg2 or whichever package you need to support whichever
relational dialect that you are using installed.  No imports call attention to the database
connectivity library, that is referenced when you run your application."""

# Think of Session and engine like global variables.  A little ghetto, but the only
# other alternative would have been a singleton design pattern.
from pprint import pprint

import sqlalchemy.sql.functions

# the db_connection.py code sets up some connection objects for us, almost like Java class variables
# that get loaded up at run time.  This statement builds the Session class and the engine object
# that we will use for interacting with the database.
from db_connection import Session, engine
# orm_base defines the Base class on which we build all of our Python classes and in so doing,
# stipulates that the schema that we're using is 'demo'.  Once that's established, any class
# that uses Base as its supertype will show up in the postgres.demo schema.
from orm_base import metadata
import logging
from sqlalchemy import Column, String, Integer, Float, UniqueConstraint, \
    Identity, ForeignKey, distinct, bindparam
from sqlalchemy.orm import relationship, backref
from orm_base import Base

from Movie import Movie
from Genre import Genre
from MovieGenre import MovieGenre

if __name__ == '__main__':
    logging.basicConfig()
    # use the logging factory to create our first logger.
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    # use the logging factory to create our second logger.
    logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)

    metadata.drop_all(bind=engine)  # start with a clean slate while in development

    # Create whatever tables are called for by our "Entity" classes.  The simple fact that
    # your classes that are subtypes of Base have been loaded by Python has populated
    # the metadata object with their definition.  So now we tell SQLAlchemy to create
    # those tables for us.
    metadata.create_all(bind=engine)

    g1: Genre = Genre(name="Thriller")
    g2: Genre = Genre(name="Romance")
    g3: Genre = Genre(name="Science Fiction")

    m1: Movie = Movie(name="Terminator II", year_released=1992, movie_rank=3.5)

    # Do our database work within a context.  This makes sure that the session gets closed
    # at the end of the with, much like what it would be like if you used a with to open a file.
    # This way, we do not have memory leaks.
    with Session() as sess:
        sess.begin()
        print("Inside the session, woo hoo.")
        sess.add(g1)
        sess.add(g2)
        sess.add(g3)
        sess.add(m1)
        # Hopefully this means that SQLAlchemy will perform the insert into movies_genres for me.
        sess.commit()
        m1.add_genre(g1)
#        sess.add(m1.genres_list[0])
        sess.commit()
        # Change the genre name and see whether we update the database.
        g2.name = 'Tragedy'
        sess.commit()
        genres: [Genre] = sess.query(Genre).all()
        for genre in genres:
            pprint(genre.__dict__)
        # Remove one of our genres just for fun
        sess.delete(genres[2])
        sess.commit()
        # We are still in a session, but I'm not going to bother committing these test genres.
        sess.add(Genre('Test Genre 1'))
        sess.add(Genre('Test Genre 2'))
        # find all test genres that I just inserted.
        genres: [Genre] = sess.query(Genre).filter(Genre.name.like('Test %'))
        print('here are the test genres')
        for genre in genres:
            print(genre)
        # See how many genres we have.
        count = sess.query(sqlalchemy.func.count(distinct(Genre.name))).one()[0]
        print('Count of genres: ', count)
        genres: [Genre] = sess.query(Genre).filter_by(name='Test Genre 2')
        print('This should be Test Genre 2', genres[0])

    print("Exiting normally.")
