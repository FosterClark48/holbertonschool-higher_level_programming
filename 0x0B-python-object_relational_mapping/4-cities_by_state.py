#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys
"""Modules which we will use to get command line args"""

"""
Makes sure that code is only executed if
the script is run directly & not imported
"""
if __name__ == '__main__':
    """Get the command line args"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """Open database connection"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=db_name)

    """Create a cursor object to iterate through db"""
    cur = db.cursor()

    """SQL query to retrieve all cities"""
    sql = "SELECT cities.id, cities.name, states.name\
            FROM cities\
            JOIN states\
            ON cities.state_id = states.id\
            ORDER BY cities.id ASC, cities.name ASC, states.name ASC;"

    """Execute SQL query with sanitization"""
    cur.execute(sql)

    """Fetch all rows and print them"""
    for row in cur.fetchall():
        print(row)

    """Close cursor and database connections"""
    cur.close()
    db.close()
