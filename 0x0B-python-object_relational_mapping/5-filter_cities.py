#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database
hbtn_0e_4_usa thats safe from SQL injections
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
    state_name = sys.argv[4]

    """Open database connection"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=db_name)

    """Create a cursor object to iterate through db"""
    cur = db.cursor()

    sql = "SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC"

    """Execute SQL query with sanitization"""
    cur.execute(sql, (state_name,))

    """Fetch all results from query and extract city names"""
    cities = cur.fetchall()
    city_names = [city[0] for city in cities]

    """Join the city names into single string with commas"""
    city_list = ", ".join(city_names)

    """
    Check if city list is empty (meaning no cities wer found)
    and print appropriate message
    """
    if city_list:
        print(city_list)
    else:
        print()

    """Close cursor and database connections"""
    cur.close()
    db.close()
