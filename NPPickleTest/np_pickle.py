import numpy as np
import pickle
from cryptography.fernet import Fernet

# File to object
x = np.load("NPPickleTest/test_X.npy")

# object to pkl bytes
pkl_x = pickle.dumps(x)

# pkl bytes encrypted
sym_key = Fernet.generate_key()
sym_key = Fernet(sym_key)
pkl_x_enc = sym_key.encrypt(pkl_x)

# decrypt pkl bytes
pkl_x_dec = sym_key.decrypt(pkl_x_enc)

# pkl bytes back to object
obj_x = pickle.loads(pkl_x_dec)


print(obj_x)





