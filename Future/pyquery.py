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


def get_all_messages(conn):
    """
    Query all rows in the history table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM history")

    rows = cur.fetchall()
    return(rows)
    # for row in rows:
    #     print(row)


def get_all_users(conn, is_Client):
    """
    Query users by is_Client
    :param conn: the Connection object
    :param is_Client:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE is_Client=?", (is_Client,))

    rows = cur.fetchall()
    return(rows)

def main():
    database = r"myapp/database.db"
    # create a database connection
    conn = create_connection(database)
    
    with conn:
        # print("1. Show all users that are clients")
        user_list = get_all_users(conn, 'True')
        # print(user_list)
        
        # print("2. Query all client messages:")
        messages_list = get_all_messages(conn)
        # print(messages_list)
        return user_list, messages_list
        
if __name__ == '__main__':
    main()
