#!/usr/bin/python3

"""script that lists all cities from the database."""

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

    cursor.execute(
                    """
                    SELECT cities.name
                    FROM cities JOIN states
                    ON states.id=cities.state_id
                    WHERE states.name = {}
                    ORDER BY cities.id ASC
                    """.format(state_name)
                )

    cities = cursor.fetchall()

    city_names = [city[0] for city in cities]

    print(city_names)

    cursor.close()
    connection.close()
