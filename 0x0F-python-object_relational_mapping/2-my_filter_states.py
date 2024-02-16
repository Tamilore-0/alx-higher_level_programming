#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


def main():
    """
    main function that displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
    """

    # store connection details
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    name_to_search = sys.argv[4]

    # Establish a connection with the MySQL databse
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    # Create a cursor object
    cursor = conn.cursor()

    cursor.execute(
        'SELECT * FROM states WHERE name \
        LIKE BINARY "{}" ORDER BY states.id ASC'.format(
            name_to_search
        )
    )

    # Fetch records from the result set
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
