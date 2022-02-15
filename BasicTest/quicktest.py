import namedtuple
import os

if __name__ == "__main__":

    if os.path.exists("test.pkl"):
        os.remove("test.pkl")

    cur_log = namedtuple.Log(False)
    cur_log.log_intent_policy_match(1, "goodAPI", [1, 2, 3])
    cur_log.log_intent_policy_mismatch(2, "badAPI", [1, 2, 3], [1, 2, 5, 6])

    # TODO: let's first try out the durable log here
    # file_to_load = open("test.pkl", "rb")
    # log_content = pickle.load(file_to_load)
    # file_to_load.close()
    items = namedtuple.loadall("test.pkl")
    for i in items:
        print(i)