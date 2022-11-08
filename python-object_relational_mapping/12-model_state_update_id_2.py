#!/usr/bin/python3
"""
Module 12-model_state_update_id_2
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """Connect to database hbtn_0e_0_usa and
    change state"""

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
    upd = ses.query(State).order_by(State.id)\
        .filter(State.id == 2).all()
    upd.name = 'Mexico'
    ses.commit()
    cont = ses.query(State).order_by(State.id).all()
    for i in cont:
        print(f"{i.id}: {i.name}")
    ses.close()
