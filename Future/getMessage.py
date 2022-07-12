import pyquery as pq
import os

def update():
    pq.update_database() # classifies messages
    # all_message = pq.get_all_messages()
    # all_users = pq.get_all_users()
    all_message = pq.get_users_messages()

    # using list comprehension convert list of tuples to list of list
    user_message_list = [list(message) for message in all_message]
    user_messages = []
    for i in user_message_list:
        # print(i[2]) # print out all client messages
        user_messages.append(i[2])
    return(user_messages)
    os._exit(100)
    
def main():
    update()
    

if __name__ == '__main__':
    main()
    


