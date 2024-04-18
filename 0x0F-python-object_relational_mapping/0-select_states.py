#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def list_states(username, password, database_name):
    """Fetches and prints all states from the specified database"""
    conn = None
    cursor = None
    try:
        # Connecting to the MySQL server
        conn = MySQLdb.connect(host='localhost', port=3306,
                               user=username, passwd=password, db=database_name)
        cursor = conn.cursor()

        # Query to fetch states
        cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
        states = cursor.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Get MySQL credentials from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Call function to list states
    list_states(mysql_username, mysql_password, database_name)
