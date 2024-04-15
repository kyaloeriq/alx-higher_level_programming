import MySQLdb
import sys

def list_states(username, password, database_name):
    # Connecting to the MySQL server
    conn = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database_name)
    cursor = conn.cursor()

    # Query to fetch states
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()
