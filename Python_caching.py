# Use lru_cache to speed up program runtime

from functools import lru_cache

@lru_cache(maxsize=16)

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

import time
t1 = time.time()

x = (fib(x) for x in range(1, 35))
print(list(x))

t2 = time.time()
print('Time taken ==> ', t2 - t1)

