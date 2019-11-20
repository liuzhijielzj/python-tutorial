from collections.abc import Iterable, Iterator
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5]) #Iterable, Iterator
print(isinstance(r, Iterator))
print(isinstance(r, Iterable))
print(list(r))
# r是一个Iterator，Iterator是惰性序列，
# 因此通过list()函数让它把整个序列都计算出来并返回一个list

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

from functools import reduce

def add(a, b):
    return a + b
print(reduce(add, [1, 2, 3, 4, 5]))

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
    #return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(list(map(lambda s: s.title(), ['adam', 'LISA', 'barT'])))

def prod(nums):
    return reduce(lambda x, y: x * y, nums)
print(prod([1, 2, 3, 4, 5]))

def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
print(list(filter(lambda s: s and s.strip(), ['A', '', 'B', None, 'C', '  '])))

'''
埃氏筛法


'''
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key = lambda item : item[0]))
print(sorted(L, key = lambda item : item[1], reverse=True))

