
storage_manager = None


class StorageManager:

    def __init__(self, config):
        self.store_location = config

    def store(self):
        if self.store_location == "nice_loc":
            print("Store successful!")
        else:
            print("oh no i failed :(")

def init_storage_manager(config):
    global storage_manager
    if storage_manager is None:
        storage_manager = StorageManager(config)
    else:
        return False
    return True

def store():
    global storage_manager
    storage_manager.store()



