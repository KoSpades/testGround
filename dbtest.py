from DBTest import database_api
from models.user import *
import os
import pickle
from cryptography.fernet import Fernet
from collections import namedtuple

TableContent = namedtuple("TableContent",
                          "content")

if __name__ == '__main__':

    # Create a key
    global_key_bytes = b'd4D2BW-Zzg3Riiw3vv78b0S8wRGpGHdc52scWvZOskQ='
    global_key = Fernet(global_key_bytes)

    # In the beginning we always remove the existing DB
    if os.path.exists("data_station.db"):
        os.remove("data_station.db")

    if os.path.exists("user_table.pkl"):
        os.remove("user_table.pkl")

    # Some insertions
    database_api.create_user(User(id=10, user_name="cat", password="123"))
    database_api.create_user(User(id=20, user_name="dog", password="123"))
    database_api.create_user(User(id=30, user_name="monkey", password="123"))
    database_api.create_user(User(id=40, user_name="sheep", password="123"))

    res = database_api.get_name_by_id_list([10, 20, 30])
    print(res)

    # res = database_api.get_all_users()
    # # Result as a list of object
    # full_table_as_list = res.data
    # # Result as plaintext bytes
    # full_table_plain_bytes = pickle.dumps(full_table_as_list)
    # # Result as ciphertext bytes
    # full_table_cipher_bytes = global_key.encrypt(full_table_plain_bytes)
    #
    # # Create TableContent
    # table_content = TableContent(content=full_table_cipher_bytes)
    #
    # # Write to file
    # with open("user_table.pkl", "ab") as f:
    #     table_to_add = pickle.dumps(table_content)
    #     f.write(table_to_add)
    #
    # # Now we test out decryption and bulk insertion
    # with open("user_table.pkl", "rb") as f:
    #     res = pickle.load(f)
    #
    # table_content_cipher = res.content
    # table_content_plain = global_key.decrypt(table_content_cipher)
    # table_content_object = pickle.loads(table_content_plain)
    #
    # # print(table_content_object)
    # # print(type(table_content_object))
    # # print(type(table_content_object[0]))
    #
    # res = database_api.recover_users(table_content_object)
    # if res == 0:
    #     res = database_api.get_all_users()
    #     # Result as a list of object
    #     full_table_as_list = res.data
    #     print(full_table_as_list)





