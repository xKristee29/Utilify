from concurrent.futures import ThreadPoolExecutor
from time import sleep

def foo(k):
    a = k
    n = 0
    for i in range(1,k):
        n = a/k
        sleep(1)
    return n


pool = ThreadPoolExecutor()

for i in range(1,10):
    future = pool.submit(foo,i)

while pool.isAlive():
    pass

print(future.result())