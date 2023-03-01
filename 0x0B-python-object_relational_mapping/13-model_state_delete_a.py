#!/usr/bin/python3
"""
Script that deletes all State objects with name
that contains letter a
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
"""
Import necessary modules for command line args
and engine/ session makers
"""

"""
Check if script is being executed as main prog or not
"""
if __name__ == '__main__':
    """Grab command line args"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """Create engine that connects to db"""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, db_name
        ), pool_pre_ping=True
    )

    """Creates table in db if one doesn't exist"""
    Base.metadata.create_all(engine)

    """Create session factory thats bound to engine"""
    Session = sessionmaker(bind=engine)

    """Creaet new session from factory"""
    session = Session()

    """Query and delete Staes w/ name containing letter a"""
    for state in session.query(State).filter(State.name.like("%a%")):
        session.delete(state)

    """Commit changes"""
    session.commit()

    """Close session"""
    session.close()
