from functools import lru_cache
#函数缓存允许我们将一个函数对于给定参数的返回值缓存起来。
# 当一个I/O密集的函数被频繁使用相同的参数调用的时候，函数缓存可以节约时间。
@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(n) for n in range(10)])

fib.cache_clear()
