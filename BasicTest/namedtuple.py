import pickle
from collections import namedtuple
import os
from cryptography.fernet import Fernet

MatchContent = namedtuple("MatchContent",
                          "status, api, accessed_DE")
MismatchContent = namedtuple("MismatchContent",
                             "status, api, accessed_DE, accessible_DE_by_policy")
IntentPolicyMatch = namedtuple('IntentPolicyMatch',
                               'caller_id, content')
IntentPolicyMismatch = namedtuple('IntentPolicyMismatch',
                                  'caller_id, content')

# initialize a global Fernet key to use
sym_key_bytes = Fernet.generate_key()
global_sym_key = Fernet(sym_key_bytes)

# initialize global flag for encrypted or not
encrypted = True

class Log:

    def __init__(self, in_memory=True, encrypted=False):
        # variable to indicate whether this log is in-memory only
        self.in_memory = in_memory
        self.encrypted = encrypted
        # Option for in-memory only log
        if in_memory:
            self.log = []
        else:
            # Initialize storage
            # TODO: read log file path from configuration
            self.log_path = "test.pkl"

    def log_intent_policy_match(self, caller_id: int, api: str, accessed_DE: [int]):
        match_content = MatchContent(status=True,
                                     api=api,
                                     accessed_DE=accessed_DE,)
        log_entry = IntentPolicyMatch(caller_id=caller_id, content=match_content)
        self._log(log_entry)

    def log_intent_policy_mismatch(self,
                                   caller_id: int,
                                   api: str,
                                   accessed_DE: [int],
                                   accessible_DE_by_policy: [int],):
        mismatch_content = MismatchContent(status=False,
                                           api=api,
                                           accessed_DE=accessed_DE,
                                           accessible_DE_by_policy=accessible_DE_by_policy,)
        log_entry = IntentPolicyMismatch(caller_id=caller_id,
                                         content=mismatch_content)
        self._log(log_entry)

    def _log(self, entry):
        if self.in_memory:
            self.log.append(entry)
        else:
            if not self.encrypted:
                with open(self.log_path, 'ab') as log:
                    entry_to_add = pickle.dumps(entry)
                    log.write(entry_to_add)
            else:
                with open(self.log_path, 'ab') as log:
                    # Look at the plaintext entry in bytes
                    entry_in_bytes = pickle.dumps(entry)
                    # print(entry_in_bytes)
                    # Look at plaintext fields
                    # print(entry.caller_id)
                    # print(entry.content)
                    # Now let's try converting entry.content to bytes
                    plain_content_in_bytes = pickle.dumps(entry.content)
                    cipher_content_in_bytes = global_sym_key.encrypt(plain_content_in_bytes)
                    # print(cipher_content_in_bytes)
                    # Let create the new log entry
                    if type(entry).__name__ == "IntentPolicyMatch":
                        encrypted_entry = IntentPolicyMatch(caller_id=entry.caller_id,
                                                            content=cipher_content_in_bytes,)
                    else:
                        encrypted_entry = IntentPolicyMismatch(caller_id=entry.caller_id,
                                                               content=cipher_content_in_bytes,)
                    encrypted_entry_in_bytes = pickle.dumps(encrypted_entry)
                    log.write(encrypted_entry_in_bytes)

    def print_log(self):
        print("Printing contents of the log:")
        for cur_entry in self.log:
            print(cur_entry)

def loadall(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break


if __name__ == "__main__":

    if os.path.exists("test.pkl"):
        os.remove("test.pkl")

    # print("First testing out durable log:")
    cur_log = Log(in_memory=False, encrypted=encrypted)
    cur_log.log_intent_policy_match(1, "goodAPI", [1, 2, 3])
    cur_log.log_intent_policy_mismatch(2, "badAPI", [1, 2, 3], [1, 2, 5, 6])

    # TODO: let's first try out the durable log here
    # file_to_load = open("test.pkl", "rb")
    # log_content = pickle.load(file_to_load)
    # file_to_load.close()
    items = loadall("test.pkl")
    for i in items:
        print("Caller ID is: ")
        print(i.caller_id)
        print("Entry content is: ")
        # Decrypting the content
        if encrypted:
            cur_plain_content_in_bytes = global_sym_key.decrypt(i.content)
            cur_content_object = pickle.loads(cur_plain_content_in_bytes)
            print(cur_content_object)

    # print("Now testing in memory log:")
    # cur_log = Log(True)
    # cur_log.log_intent_policy_match(1, "goodAPI", [1, 2, 3])
    # cur_log.log_intent_policy_mismatch(2, "badAPI", [1, 2, 3], [1, 2, 5, 6])
    # cur_log.print_log()
