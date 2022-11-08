#!/usr/bin/python3
"""
Module 9-model_state_filter_a
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
    for i in ses.query(State).order_by(State.id)\
            .filter(State.name.like('%a%')).all():
        print(f"{i.id}: {i.name}")
    ses.close()
