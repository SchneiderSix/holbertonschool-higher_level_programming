#!/usr/bin/python3
"""
Module 1-filter_states
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Connect to database hbtn_0e_0_usa and list names starting with N"""
    try:
        db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                             passwd=argv[2], db=argv[3])
    except Exception:
        print("Error")

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    cont = cursor.fetchall()

    for i in cont:
        if i[1].startswith("N"):
            print(i)

    db.close()
