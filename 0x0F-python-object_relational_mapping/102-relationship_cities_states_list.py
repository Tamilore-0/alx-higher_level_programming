#!/usr/bin/python3
"""
A script that prints all City objects
from the database hbtn_0e_14_usa
"""


import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker


def main():
    """
    main function that prints all City objects
    from the database hbtn_0e_14_usa
    """
    # Creating a connection to MySQL server using mysql-python DBAPI
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database_name
        ), pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    # Create a new session object bound to the engine
    with sessionmaker(bind=engine)() as session:
        states = session.query(State).order_by(asc(State.id))
        for state in states:
            for city in state.cities:
                print(f"{city.name} -> {state.name}")


if __name__ == '__main__':
    # Store connection details
    if (len(sys.argv) == 4):
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
    else:
        print("Incomplete arguments")
    # Call the main function if the script is executed directly
    main()
