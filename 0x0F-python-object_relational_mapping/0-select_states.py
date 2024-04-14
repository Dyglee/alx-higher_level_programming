#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
