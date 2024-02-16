#!/usr/bin/python3
"""
A script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine, asc, func
from sqlalchemy.orm import sessionmaker, Session


def main():
    """
    Main function that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa
    """
    # Store connection details
    if (len(sys.argv) == 5):
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
        # create new State object
        new_state = State(name='Louisiana')

        # Add the new State to the session
        session.add(new_state)

        # Commit the transaction to the database
        session.commit()
        print(new_state.id)


if __name__ == '__main__':
    # Call the main function if the script is executed directly
    main()
