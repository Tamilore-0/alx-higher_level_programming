#!/usr/bin/python3
"""
A script that changes the name of a State
object from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    Main function script that changes the name
    of a State object from the database hbtn_0e_6_usa
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
        # Update object whose id is 2
        record = session.query(State).filter(State.id == 2).first()

        if record:
            record.name = "New Mexico"
            # Kepp changes
            session.commit()


if __name__ == '__main__':
    # Call the main function if the script is executed directly
    main()
