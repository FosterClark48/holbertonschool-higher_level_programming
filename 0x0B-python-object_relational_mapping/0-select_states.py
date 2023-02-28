#!/usr/bin/python3
""" Script that lists all states from database hbtn_0e_0_usa """

"""Modules which we will use to get command line args"""
import MySQLdb
import sys

"""
Makes sure that code is only executed if
the script is run directly & not imported
"""
if __name__=='__main__':
    """
    Get the command line args for MySQL username, password,
    and database name. These arguments are passed in when
    the script is run from the command line
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """
    Connect to the MySQL server running on localhost at port 3306
    using the mySQLdb.connect() method. Pass in the username,
    password, and database name that we got from command line args
    """
    db = MySQLdb.connect(host='localhost', port=3306,
                        user=username, passwd=password, db=db_name)

    """
    Create a cursor object using cursor() method of the connection object
    """
    cur = db.cursor()

    """
    Execute SQL query using execute() method of cursor object.
    Query selects all rows from states table in hbtn_0e_0_usa
    database,sorted in ascending order by states.id.
    """
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    """
    Iterate over results w/ for loop and fetchall() method
    of the cursor object. fetchall() returns all rows in result
    set as a list of tuples.
    """
    for row in cur.fetchall():
        print(row)

    """
    Close cursor and database connections using the close() method.
    """
    cur.close()
    db.close()
