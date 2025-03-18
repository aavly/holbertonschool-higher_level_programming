#!/usr/bin/python3
""" 12. Update a new state """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":

    database_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(database_uri)

    Session = sessionmaker(bind=engine)
    session = Session()

    # retrieve state oject
    state_to_update = session.query(State).filter(State.id == 2).first()

    if state_to_update:
        state_to_update.name = 'New Mexico'

    # REMEMBER TO SAVE CHANGES TO DATABASE
    session.commit()

    states = session.query(State).order_by(State.id).all()
    # print results
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
