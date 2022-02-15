import random
from statistics import mean

def throwdice(start_val):
    cur_sum = 0
    cur_throw = random.randint(1, 6)
    cur_mod = (start_val + cur_throw) % 3
    if cur_mod == 0:
        return cur_sum
    else:
        cur_sum += 1
        return cur_sum + throwdice(cur_mod)


res_list = []
for _ in range(10000):
    res_list.append(throwdice(0))

print(mean(res_list))
