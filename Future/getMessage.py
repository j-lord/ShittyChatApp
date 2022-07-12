from pickletools import pytuple
import pyquery as pq
import os

# users, messages = pq.main()
# print(users, messages)

# all_message = pq.get_all_messages() # Works
# all_users = pq.get_all_users()
# all_message = pq.get_all_messages() # Works
all_user_messages = pq.get_users_messages()
print(list(all_user_messages[0])[2])
# print(pq.all_user_messages())
os._exit(100)

