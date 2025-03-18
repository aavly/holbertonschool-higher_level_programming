#!/usr/bin/python3
""" 2. Filter states by user input """

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
    user_input_state_name = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name = '{}'\
        ORDER BY id".format(user_input_state_name))
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
