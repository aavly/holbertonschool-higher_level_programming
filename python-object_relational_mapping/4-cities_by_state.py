#!/usr/bin/python3
""" 4. Cities by states """

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
    query = "SELECT * FROM states ORDER BY id"
    cur.execute(query)
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
