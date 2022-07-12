import pyquery as pq
import os

# users, messages = pq.main()
# print(users, messages)

# all_message = pq.get_all_messages() # Works
# all_users = pq.get_all_users()    # Works
all_message = pq.get_users_messages() # Works

# using list comprehension
# convert list of tuples to list of list
user_message_list = [list(message) for message in all_message]
for i in user_message_list:
    print(i[2])
# print out all client messages

os._exit(100)

