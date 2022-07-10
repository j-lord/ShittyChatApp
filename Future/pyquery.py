import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def select_all_users(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM user")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_task_by_is_Client(conn, is_Client):
    """
    Query tasks by is_Client
    :param conn: the Connection object
    :param is_Client:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE is_Client=?", (is_Client,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = r"myapp/database.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by is_Client:") # see if message is from client
        select_task_by_is_Client(conn, 1)

        # print("2. Query all tasks")
        select_all_users(conn)


if __name__ == '__main__':
    main()
