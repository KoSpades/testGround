import time
from multiprocessing import Process, freeze_support


def f(a, b):
    print("xxxxxxxx")

def call_api(api, cur_username, *args, **kwargs):
    print("check")
    interceptor_process = Process(target=f, args=("", ""))
    time.sleep(5)
    interceptor_process.start()
    interceptor_process.join()


if __name__ == '__main__':
    call_api("", "")
