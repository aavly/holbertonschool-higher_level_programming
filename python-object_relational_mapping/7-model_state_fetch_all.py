#!/usr/bin/python3
""" 7. All states via SQLAlchemy """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    
    # create an enginer to connect to MySQL
    database_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(database_uri)
    
    # bind the engine to the session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # query all states and order by id
    states = session.query(State).order_by(State.id).all()
    
    # print results
    for state in states:
        print(f"{state.id}: {state.name}")

    # close session
    session.close()