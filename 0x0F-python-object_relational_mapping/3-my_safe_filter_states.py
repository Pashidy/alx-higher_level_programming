#!/usr/bin/python3
"""  Lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    match = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (f"%{match}%",))  # Adding '%' for wildcard search
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
