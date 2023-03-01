#!/usr/bin/python3
"""
Python file that contains class definition of City
and an instance of Base = declarative_base()
"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from model_state import Base
"""Import modules necessary to create subclass and base instance"""


class City(Base):
    """Name of table in database to link to"""
    __tablename__ = "cities"

    """
    Define columns for table
    id represents column of auto-generated, unique int, cant be null, primary
    name represents column of 128 char string and cant be null
    state_id represeents column of int, not null, foreign key to states.id
    """
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
