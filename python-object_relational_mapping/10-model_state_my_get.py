#!/usr/bin/python3
"""
Module 10-model_state_my_get
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """Connect to database hbtn_0e_0_usa and
    lists all cities from the database"""

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
    cont = ses.query(State).order_by(State.id)\
          .filter(State.name == argv[4]).all()
    if cont:
        print(f"{cont.id}")
    else:
        print("Not found")
    ses.close()
