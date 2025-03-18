#!/usr/bin/python3
""" 14. Cities in state model file """


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State



class City(Base):
    """ City class thank links to the MySQL table 'cities' """
    __tablename__ = 'cities'
    
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column( ForeignKey("states.id"), Integer, nullable=False)
    
    state = relationship('State', backref='cities')
