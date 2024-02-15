#!/usr/bin/python3
"""
A script to connect to a MySQL database and fetch data from the 'states' table.
"""


import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and fetches data from the 'states' table.

    Usage: python3 script.py <username> <password> <database_name>

    Arguments:
        username: Username for accessing the MySQL database.
        password: Password for accessing the MySQL database.
        database_name: Name of the MySQL database to connect to.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Establish a connection to the MySQL database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM states ORDER BY states.id ASC')

    # Fetch all rows from the result set
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
