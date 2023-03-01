#!/usr/bin/python3
"""
Script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

    """Create the necessary tables in the database if not exists"""
    Base.metadata.create_all(engine)

    """Create a session factory bound to the engine"""
    Session = sessionmaker(bind=engine)

    """Create a new session from the factory"""
    session = Session()

    """
    Create new state named Louisiana w/ id of 6
    """
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    """Print new states.id"""
    print(new_state.id)
