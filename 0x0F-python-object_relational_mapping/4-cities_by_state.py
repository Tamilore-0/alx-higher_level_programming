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

    cursor.execute(
        'SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC'
    )

    # Fetch records from result set
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
