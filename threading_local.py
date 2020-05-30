# a = {
#     250:{},#request
#     290: {},  # request
# }
import threading
import time
from threading import local

# s_local=local()
# s_local.name=1

def func(num):
    num+=1
    time.sleep(1)
    print(num, threading.current_thread().name, threading.current_thread().ident)
    return num

if __name__ == '__main__':
    for num in range(20):
        th = threading.Thread(target=func, args=(num,))
        th.start()