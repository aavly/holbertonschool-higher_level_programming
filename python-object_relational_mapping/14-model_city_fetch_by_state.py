#!/usr/bin/python3
""" 14. Cities in state """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City

if __name__ == "__main__":

    database_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(database_uri)

    Session = sessionmaker(bind=engine)
    session = Session()

    # query all cities and join with states
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # print results
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
