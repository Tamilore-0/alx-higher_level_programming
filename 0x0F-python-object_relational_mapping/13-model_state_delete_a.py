#!/usr/bin/python3
"""
A script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker


def main():
    """
    Main function that deletes all State objects with a name
    containing the letter a from the database hbtn_0e_6_usa
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
        # Searches for states containing 'a'
        records = session.query(State). \
            filter(func.binary(State.name).like('%a%'))
        # Deletes found objects
        if records:
            for record in records:
                session.delete(record)
            session.commit()


if __name__ == '__main__':
    # Call the main function if the script is executed directly
    main()
