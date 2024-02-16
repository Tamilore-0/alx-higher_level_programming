#!/usr/bin/python3
"""
A script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def main():
    """
    Main function to connect to the MySQL database and list all states
    with a name starting with 'N' (upper case) from the specified database.
    """
    # collect connection detail from cmd
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Establish a connection to the MySQL database
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    # Create the cursor object
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM states WHERE name \
        LIKE BINARY "N%" ORDER BY states.id ASC'
    )

    # Fetch all rows from the result set
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
