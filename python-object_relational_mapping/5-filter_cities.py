#!/usr/bin/python3
""" 5. All cities by state """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306, user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()

	# PARAMETISED QUERIES TO PROJECT FROM SQL INJECTIONS
    user_input_state_name = sys.argv[4]

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id
    """

    cur.execute(query, (user_input_state_name,))

    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
