#!/usr/bin/python3
"""
A script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine, asc, func
from sqlalchemy.orm import sessionmaker, Session


def main():
    """
    Main function that lists all State objects that
    contain the letter a from the database hbtn_0e_6_usa.
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
        # Search for states that contain "a"
        records = session.query(State).filter(
            func.binary(State.name).like('%a%')
        ).order_by(asc(State.id))

        if records:
            # Print states that contain "a"
            for record in records:
                print(f"{record.id}: {record.name}")


if __name__ == '__main__':
    # Call the main function if the script is executed directly
    main()
