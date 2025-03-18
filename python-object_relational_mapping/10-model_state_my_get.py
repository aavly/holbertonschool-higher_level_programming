#!/usr/bin/python3
""" 10. Get a state """

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

    # user input as 3rd parameter
    user_input_state_name = argv[4]

    # query all states and order by id
    state = session.query(State).filter(State.name == user_input_state_name)\
        .first()

    # print results
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # close session
    session.close()
