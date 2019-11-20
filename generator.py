# 把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))
print(type(g))
print(next(g))
print(next(g))
print(next(g))

for n in g:
    # next(g)
    # StopIteration if no more
    print(n)

'''
generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现
'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        print('after yield')
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(6):
    print(n)
# no return value 'done' is gotten
g = fib(6)
while True:
    try:
        x = next(g)
        print('g: ', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
next(o)
next(o)
next(o)
