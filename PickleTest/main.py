import numpy as np
import pickle
from cryptography.fernet import Fernet

cur_file_path = "train0_X.npy"

with open(cur_file_path, "rb") as f:
    cur_bytes = f.read()

cur_np_obj = np.load(cur_file_path)
# print(cur_np_obj)
cur_pkl_obj = pickle.dumps(cur_np_obj)
print(len(cur_pkl_obj))
print(cur_pkl_obj[:100])
# print(cur_pkl_obj)
# print(cur_bytes == cur_pkl_obj)

sym_key = Fernet.generate_key()
f = Fernet(sym_key)
ciphertext_from_bytes = f.encrypt(cur_bytes)
ciphertext_from_pkl = f.encrypt(cur_pkl_obj)
# print(ciphertext_from_pkl == ciphertext_from_bytes)

plainttext_from_pkl = f.decrypt(ciphertext_from_pkl)
print(len(plainttext_from_pkl))
print(plainttext_from_pkl[:100])
plaintext_pkl_obj = pickle.loads(plainttext_from_pkl)
# print(cur_np_obj == plaintext_pkl_obj)

