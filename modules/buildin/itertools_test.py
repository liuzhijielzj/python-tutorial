import itertools

natuals = itertools.count(1)
cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)

ns = itertools.repeat('A', 3)
for n in ns:
    print(n)

ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
    print(n)

# 一组迭代对象串联起来
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# 相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))


'''
挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，
这两个元素就被认为是在一组的，而函数返回值作为组的key。
如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key
'''
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))