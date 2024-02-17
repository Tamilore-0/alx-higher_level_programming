#!/usr/bin/python3
"""
Define State class and Base instance
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Create declarative base class for mapping
Base = declarative_base()


class State(Base):
    """
    State class representing the states table in the database
    """
    __tablename__ = 'states'

    id = Column(
        Integer,
        autoincrement=True,
        nullable=False,
        primary_key=True
    )

    name = Column(
        String(128),
        nullable=False
    )
