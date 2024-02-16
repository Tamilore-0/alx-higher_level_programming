#!/usr/bin/python3
"""
A script that prints the first State object from the database hbtn_0e_6_usa.
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def main():
    """
    Main function that prints the first State
    object from the database hbtn_0e_6_usa.
    """
    # Store connection details
    if (len(sys.argv) == 4):
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
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
        # Query all states from the 'states' table and print their IDs
        record = session.query(State).first()
        if (record is None):
            print("Nothing")
        else:
            print(f"{record.id}: {record.name}")


if __name__ == '__main__':
    # Call the main function if the script is executed directly
    main()
