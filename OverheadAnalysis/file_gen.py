with open('my_file.txt', 'wb') as f:
    num_chars = 1024
    for i in range(num_chars):
        f.write(b'\x11')
