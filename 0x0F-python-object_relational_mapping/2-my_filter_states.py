#!/usr/bin/python3

"""displays all values in the states table where name matches the argument."""

import sys
import MySQLdb


if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    state_name = sys.argv[4]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM states
            WHERE name LIKE BINARY '{}'
            ORDER BY states.id ASC""".format(state_name))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()
