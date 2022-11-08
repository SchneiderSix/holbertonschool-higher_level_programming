#!/usr/bin/python3
"""
Module 5-filter_cities
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Connect to database hbtn_0e_0_usa and list all
    cities of that state"""

    try:
        db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                             passwd=argv[2], db=argv[3])
    except Exception:
        print("Error")

    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM cities \
                    JOIN states ON  cities.state_id = states.id WHERE \
                    BINARY states.name = %s""", (argv[4],))
    cont = cursor.fetchall()

    for i in cont:
        for j in i:
            if i != 1 and i != len(cont):
                print(", ", end='')
            print(j, end='')
    print()
    cursor.close()
    db.close()
