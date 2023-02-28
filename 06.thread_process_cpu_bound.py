import time
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import sys

PRIMES = [112272535095293] * 50

# 单线程、多线程、多进程对比CPU密集计算速度
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def single_thread():
    for num in PRIMES:
        is_prime(num)

def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)
        
def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


def how_much_time(func, func_name):   # 语法糖
    def inner():
        start = time.time()
        func()
        end = time.time()
        print("{0:^14}花费{1:}秒".format(func_name, end - start, ))
    return inner


if __name__ == "__main__":
    single_thread = how_much_time(single_thread, "single_thread")   # 22.864226579666138秒
    multi_thread = how_much_time(multi_thread, "multi_thread")   # 23.27589249610901秒
    multi_process = how_much_time(multi_process, "multi_process")   # 4.868769884109497秒
    single_thread()
    multi_thread()
    multi_process()
    
    
    # start = time.time()
    # multi_process()
    # end = time.time()
    # print("multi process:", end - start) 
