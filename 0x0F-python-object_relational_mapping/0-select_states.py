#!/usr/bin/python3

"""script that lists all states from the database."""

import sys
import MySQLdb


if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()
