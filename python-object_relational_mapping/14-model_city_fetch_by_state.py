#!/usr/bin/python3
"""
Module 14-model_city_fetch_by_state
"""

from sys import argv
from model_city import Base, City
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
    for i, j in ses.query(State, City).\
            filter(State.id == City.state_id):
        print(f"{i.name}: ({j.id}) {j.name}")
    ses.close()
