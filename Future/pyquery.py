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

def get_all_messages():
    """
    Query all rows in the history table
    :param None:
    :return: Tuple of messages
    """
    database = r"myapp/database.db"
    # create a database connection
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT * FROM history")

    rows = cur.fetchall()
    return(rows)

def get_all_users():
    """
    Query users by is_Client
    :param None: 
    :return: Tuple of users
    """
    database = r"myapp/database.db"
    # create a database connection
    conn = create_connection(database)

    cur = conn.cursor()
    # cur.execute("SELECT * FROM user WHERE is_Client=?", (is_Client,))
    cur.execute("SELECT * FROM user WHERE is_Client='True'")

    rows = cur.fetchall()
    return(rows)

def get_users_messages():
    """
    Query all messages
    :param None:
    :return: Tuple of messages
    """
    database = r"myapp/database.db"
    # create a database connection
    conn = create_connection(database)

    cur = conn.cursor()
    # cur.execute("SELECT * FROM user WHERE is_Client=?", (is_Client,))
    cur.execute("SELECT * FROM history WHERE is_Client_Message='True'")

    rows = cur.fetchall()
    return(rows)

def update_database():
    database = r"myapp/database.db"
    conn = create_connection(database)
    cur = conn.cursor()
    
    sql_command = """UPDATE history
    SET is_Client_Message = "NULL" WHERE id = 1
    """
    sql_command = """UPDATE history
            SET is_Client_Message = (
            SELECT is_Client 
            FROM user
            WHERE username = history.user);

    """
    cur.execute(sql_command)
    conn.commit()
    conn.close
#     cur.execute("-- UPDATE history
# --     SET is_Client_Message = (
# --         SELECT is_Client 
# --         FROM user
# --         WHERE username = history.user);
# ")

def main():
    database = r"myapp/database.db"
    # create a database connection
    conn = create_connection(database)
    
    with conn:
        # print("1. Show all users that are clients")
        # user_list = get_all_users(conn, 'True')
        # print(user_list)
        
        # print("2. Query all client messages:")
        # messages_list = get_all_messages(conn)
        # print(messages_list)
        # return user_list, messages_list
        print()
        
if __name__ == '__main__':
    main()
