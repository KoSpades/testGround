def recur_mut(val, arr):
    if val > 1:
        arr.append(val)
        recur_mut(val-1, arr)

def try_mutate():
    arr = []
    recur_mut(5, arr)
    return arr

print(try_mutate())
