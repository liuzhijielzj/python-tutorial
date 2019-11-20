def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        print('after yield')
        a, b = b, a + b
        n = n + 1
    return 'done'

generator = fib(3)
print(next(generator))
print(next(generator))