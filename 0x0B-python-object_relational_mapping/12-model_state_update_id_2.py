#!/usr/bin/python3
"""
Script that changes the name of a State object
from database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
"""
Importing necessary modules for connecting to server and
creating command line args
"""

"""don't execute program if imported as module, only as main prog"""
if __name__ == '__main__':
    """get command line args"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """Open database connection"""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, db_name), pool_pre_ping=True)

    """Create table in database if not exists"""
    Base.metadata.create_all(engine)

    """Create session factory bound to engine"""
    Session = sessionmaker(bind=engine)

    """Create new session from session factory"""
    session = Session()

    """update State object with id of 2"""
    update_state = session.query(State).filter(State.id == 2).first()

    """change queried name to New Mexico"""
    update_state.name = "New Mexico"

    """Commit the changes"""
    session.commit()

    """Close session"""
    session.close()
