"""This "application" is a demonstration using SQLAlchemy to create a small number of tables and populate
them.  Not evey possible use case for SQLAlchemy is explored in this demonstration, only those which are
required for this particular demonstration.

Technical Note: Be sure to have psycopg2 or whichever package you need to support whichever
relational dialect that you are using installed.  No imports call attention to the database
connectivity library, that is referenced when you run your entine."""

# Think of Session and engine like global variables.  A little ghetto, but the only
# other alternative would have been a singleton design pattern.

# the db_connection.py code sets up some connection objects for us, almost like Java class variables
# that get loaded up at run time.  This statement builds the Session class and the engine object
# that we will use for interacting with the database.
from db_connection import Session, engine
# orm_base defines the Base class on which we build all of our Python classes and in so doing,
# stipulates that the schema that we're using is 'demo'.  Once that's established, any class
# that uses Base as its supertype will show up in the postgres.demo schema.
from orm_base import metadata
import logging
from Section import Section
from Student import Student
from Enrollment import Enrollment


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

    s1: Section = Section("CECS", "101", 1, "Fall", 2022)
    s2: Section = Section("CECS", "101", 2, "Fall", 2022)

    t1: Student = Student("John", "Doe")
    t2: Student = Student("Jane", "Doe")

    # Do our database work within a context.  This makes sure that the session gets closed
    # at the end of the with, much like what it would be like if you used a with to open a file.
    # This way, we do not have memory leaks.
    with Session() as sess:
        sess.begin()
        print ("Inside the session, woo hoo.")
        sess.add(s1)
        sess.add(s2)
        sess.add(t1)
        sess.add(t2)
        sess.commit()
        t1.add_SectionToStudent(s1)
        t2.add_SectionToStudent(s2)
        sess.commit()
        print("Done with the session, bye bye.")





        # Now we're going to create a section and enroll a student in it.
    print("Exiting normally.")
