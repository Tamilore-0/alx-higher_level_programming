#!/usr/bin/python3
"""
Define City class
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    City class representing the cities table in the database
    """
    __tablename__ = 'cities'

    id = Column(
        Integer,
        autoincrement=True,
        nullable=False,
        primary_key=True,
    )

    name = Column(
        String(128),
        nullable=False
    )

    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        unique=True,
        nullable=False
    )

    state = relationship("State")
