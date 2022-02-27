import numpy as np

from cryptography.fernet import Fernet

# pkl bytes encrypted
sym_key = Fernet.generate_key()
sym_key = Fernet(sym_key)

with open("NPPickleTest/test_X.npy", "rb") as f:
    data = f.read()
    enc_data = sym_key.encrypt(data)

with open("NPPickleTest/enc_x.npy", "wb") as f:
    f.write(enc_data)

temp = np.load("NPPickleTest/enc_x.npy")
