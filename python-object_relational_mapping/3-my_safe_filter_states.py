#!/usr/bin/python3
"""
Module 3-my_safe_filter_states
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Connect to database hbtn_0e_0_usa and list names
    starting with N, safe for sqlinjection"""
    if len(argv) == 5:
        try:
            db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                                passwd=argv[2], db=argv[3])
        except Exception:
            print("Error")

        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE \
                        name LIKE BINARY '{}'".format(argv[4]))
        cont = cursor.fetchall()

        for i in cont:
            print(i)
        db.close()
    else:
        pass
