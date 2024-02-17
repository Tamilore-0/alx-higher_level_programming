#!/usr/bin/python3
"""
Define City class
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
    City class representing the cities table in the database
    """
    __tablename__ = 'cities'

    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
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
        nullable=False
    )
