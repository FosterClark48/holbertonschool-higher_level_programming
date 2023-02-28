#!/usr/bin/python3
"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument
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

    """Connect to the MySQL server"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=db_name)

    """Create a cursor object to iterate through db"""
    cur = db.cursor()

    """Execute SQL query"""
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                ORDER BY states.id ASC;".format(sys.argv[4]))

    """Fetch all rows and print them"""
    for row in cur.fetchall():
        print(row)

    """Close cursor and database connections"""
    cur.close()
    db.close()
