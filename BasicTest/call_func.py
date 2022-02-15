def call_func(func_name, *args, **kwargs):
    return func_name(*args, **kwargs)

def nice_func(low, med, high):
    print("low number is "+str(low))
    print("mid number is "+str(med))
    print("high number is "+str(high))


def random_func(power):
    print(2**power)


call_func(random_func, 1)
call_func(nice_func, 2, 5, 10)
