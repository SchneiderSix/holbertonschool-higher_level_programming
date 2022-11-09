#!/usr/bin/python3
"""
Module model_city
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """ORM Class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                autoincrement=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
