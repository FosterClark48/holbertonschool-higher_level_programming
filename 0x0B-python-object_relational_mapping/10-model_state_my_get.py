#!/usr/bin/python3
"""
Script that prints the State object with the name
passed as an argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
"""
Modules which we will use to get command line args
and create engines and sessions and access base/state classes
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
    state_name = sys.argv[4]

    """Open database connection by creating engine"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    """Create a session factory bound to the engine"""
    Session = sessionmaker(bind=engine)

    """Create a new session from the factory"""
    session = Session()

    """
    Query the database for State objects with specified name
    """
    states = session.query(State).filter(State.name == state_name).all()

    """
    Print id of each State object returned by query
    or "Not found" if no results were found
    """
    if len(states) == 0:
        print("Not found")
    else:
        for state in states:
            print(state.id)

    """close session"""
    session.close()
