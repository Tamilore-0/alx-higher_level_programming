#!/usr/bin/python3
"""
A script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine, asc, func
from sqlalchemy.orm import sessionmaker, Session


def main():
    """
    Main function that prints the State object with the
    name passed as argument from the database hbtn_0e_6_usa
    """
    # Store connection details
    if (len(sys.argv) == 5):
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        state_to_search = sys.argv[4]
    else:
        print("Incomplete arguments")

    # Creating a connection to MySQL server using mysql-python DBAPI
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database_name
        ), pool_pre_ping=True
    )

    # Create a new session object bound to the engine
    with sessionmaker(bind=engine)() as session:
        # Searches for states that match the required state
        record = session.query(State).filter(
            State.name == state_to_search
        ).first()

        if record is None:
            print("Not found")
        else:
            print(record.id)


if __name__ == '__main__':
    # Call the main function if the script is executed directly
    main()
