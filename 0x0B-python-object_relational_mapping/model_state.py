#!/usr/bin/python3
"""
File that contains the class definition of a State
and an instance of Base = declarative_base()
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
"""Imported necessary sqlalchemy modules"""

"""
Declare a base class that State class will inherit from
This is necessary for SQLAlchemy's ORM to work properly
"""
Base = declarative_base()


"""Define State class that represents table in database"""
class State(Base):
    """Name of table in database"""
    __tablename__ = 'states'

    """
    Define columns for table
    id is an auto-generated, unique int that serves as Primary key
    name is a string with max length of 128 chars
    """
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
