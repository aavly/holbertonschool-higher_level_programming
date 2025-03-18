#!/usr/bin/python3
""" 11. Add a new state """

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

    # adding a state
    new_state = State(name='Louisiana')
    session.add(new_state)

    # print results
    print(new_state.id)

    # close session
    session.close()
