#!/usr/bin/python3
"""
Script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
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

    """Open database connection by creating engine"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name), pool_pre_ping=True)

    """Create a session factory bound to the engine"""
    Session = sessionmaker(bind=engine)

    """Create a new session from the factory"""
    session = Session()

    """
    Query first state object from db hbtn_0e_6_usa by state.id
    """
    states_a = session.query(State)\
        .filter(State.name.like("%a%")).order_by(State.id).all()

    """Iterate through results and print"""
    for state in states_a:
        print("{}: {}".format(state.id, state.name))

    """close session"""
    session.close()
