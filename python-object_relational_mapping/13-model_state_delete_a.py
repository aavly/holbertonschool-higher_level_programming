#!/usr/bin/python3
""" 13. Delete states """

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

    try:
        # retrieve state oject
        states_to_delete = session.query(State).filter(
            State.name.like('%a%')).all()

        # deleting states if exists
        if states_to_delete:
            for state in states_to_delete:
                session.delete(state)

        # REMEMBER TO SAVE CHANGES TO DATABASE
        session.commit()

        states = session.query(State).order_by(State.id).all()
        # print results
        for state in states:
            print(f"{state.id}: {state.name}")

    finally:
        session.close()
