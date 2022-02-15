ifile = open("original.txt", 'rb').read()

ciphertext_bytes = sym_key.encrypt(ifile)

file = open("cipher.txt", "wb")
file.write(ciphertext_bytes)
file.close()
