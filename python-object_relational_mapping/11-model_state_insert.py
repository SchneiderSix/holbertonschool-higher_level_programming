#!/usr/bin/python3
"""
Module 11-model_state_insert
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """Connect to database hbtn_0e_0_usa and
    add state"""

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
    lou = State(name='Louisiana')
    ses.add(lou)
    ses.commit()
    for i in ses.query(State).order_by(State.id).all():
        print(f"{i.id}: {i.name}")
    ses.close()
