#!/usr/bin/python3
"""
Module 13-model_state_delete_a
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """Connect to database hbtn_0e_0_usa and
    delete state"""

    try:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True
        )
    except Exception:
        print("Error")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    ses = Session()
    for i in ses.query(State).filter(State.name.ilike('%a%')):
        ses.delete(i)
    ses.commit()
    ses.close()
