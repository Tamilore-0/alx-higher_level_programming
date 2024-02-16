#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa.
"""


import MySQLdb
import sys


def main():
    """
    Main function that lists all cities from the database hbtn_0e_4_usa
    """
    # Store connection details
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Establish a connection with MySQL database
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Get the id of specified state
    cursor.execute(
        'SELECT id FROM states WHERE name LIKE BINARY %s', (state_name,)
    )
    states_id = cursor.fetchone()

    # Find cities under the same id
    if states_id:
        cursor.execute(
            'SELECT name FROM cities WHERE state_id = %s', (states_id,)
        )
        records = cursor.fetchall()
        if records:
            for row in records:
                if (row != records[0]):
                    print(', ', end='')
                print(row[0], end='')
    print()

    # Fetch records from result set
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
