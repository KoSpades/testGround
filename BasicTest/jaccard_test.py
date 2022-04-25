import random
import statistics

hash_val = [1, 2, 3, 4]

list_a = [0, 1]
list_b = [2, 3]

total_match = 0
num_run = 10000

for i in range(num_run):
    random.shuffle(hash_val)
    med_a = int(statistics.median(hash_val[:len(list_a)]))
    med_b = int(statistics.median(hash_val[2:len(list_b)+2]))
    # print(med_a)
    # print(med_b)
    if med_a == med_b:
        total_match += 1

print(total_match/num_run)


