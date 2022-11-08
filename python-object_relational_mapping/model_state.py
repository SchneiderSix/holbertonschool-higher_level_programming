#!/usr/bin/python3
"""
Module model_state
"""

import MySQLdb

Base = declarative_base()

class State(Base):
    """ORM Class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                autoincrement=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
