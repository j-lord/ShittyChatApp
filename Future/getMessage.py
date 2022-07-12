import pyquery as pq
import os

# users, messages = pq.main()
# print(users, messages)
all_message = pq.get_all_messages_test()
print(all_message)
os._exit(100)