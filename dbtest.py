from writeaheadlog.write_ahead_log import WAL
from DBTest import database_api
from models.user import *
import os

if __name__ == '__main__':

    cur_WAL = WAL()

    if os.path.exists("data_station.db"):
        os.remove("data_station.db")

    # my_str_1 = database_api.create_user(User(user_name="cat", password="123"), cur_WAL)

    cur_WAL.recover_db_from_wal()
