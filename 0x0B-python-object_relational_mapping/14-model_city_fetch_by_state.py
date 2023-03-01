#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
"""
Modules which we will use to get command line args
and create engines and sessions and access base/city classes
"""

"""
if executed as a main program, not as a module imported by another
scirpt
"""
if __name__ == '__main__':
    """Get the command line args"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """Open database connection by creating engine"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name), pool_pre_ping=True)

    """Create a session factory bound to the engine"""
    Session = sessionmaker(bind=engine)

    """Create a new session from the factory"""
    session = Session()

    """
    Query all City objects from database and sort in asc order by cities.id
    """
    cities = session.query(City, State).join(State).order_by(City.id).all()

    """Print results"""
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    """close session"""
    session.close()
