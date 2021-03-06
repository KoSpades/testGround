import pickle
from collections import namedtuple
from DBTest import database_api
from models.user import *

WriteContent = namedtuple("WriteContent",
                          "caller_id, content")

class WAL:

    def __init__(self):
        # TODO: change this to using config
        self.wal_path = "wal.pkl"

    def log(self, caller_id, entry):
        # print(caller_id)
        write_content = WriteContent(caller_id=caller_id,
                                     content=entry)
        with open(self.wal_path, 'ab') as log:
            entry_to_add = pickle.dumps(write_content)
            log.write(entry_to_add)

    def read_wal(self):
        entries = self.loadall(self.wal_path)
        for cur_entry in entries:
            print(cur_entry)

    def recover_db_from_wal(self):
        entries = self.loadall(self.wal_path)
        for cur_entry in entries:
            print(cur_entry)
            # exec(cur_entry)

    @staticmethod
    def loadall(filename):
        with open(filename, "rb") as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break
