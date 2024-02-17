#!/usr/bin/python3
"""
A script that prints all City objects
from the database hbtn_0e_14_usa
"""


import sys
from model_state import Base, State
from model_city import City
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

    # Create a new session object bound to the engine
    with sessionmaker(bind=engine)() as session:
        # JOINS city and state table together to obtain result
        record = session.query(State, City).join(City).order_by(asc(City.id))
        for state, city in record:
            print(f"{state.name}: ({city.id}) {city.name}")


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
