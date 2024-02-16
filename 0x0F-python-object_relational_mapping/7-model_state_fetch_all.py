#!/usr/bin/python3
"""
A script that connects to a MySQL database and retrieves all
states from the 'states' table, printing their IDs and names.
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def main():
    # Store connection details
    if (len(sys.argv) == 4):
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
    else:
        print("Incomplete arguments")

    # Connecting to MySQL server using mysql-python DBAPI
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database_name
        ), pool_pre_ping=True
    )

    # Create a new session object bound to the engine
    session = sessionmaker(bind=engine)()
    # Query all states from the 'states' table and print their IDs
    for instance in session.query(State).order_by(State.id):
        print(f"{instance.id}: {instance.name}")


if __name__ == '__main__':
    # Call the main function if the script is executed directly
    main()
