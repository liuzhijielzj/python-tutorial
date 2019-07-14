'''
在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”
'''
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9) #当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
print(f1 == f2)

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

#9, 9, 9
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

# def createCounter(start = 1):
#     def counter(n):
#         sum = n
#         def addOne():
#             sum = sum + 1
#             return sum
#         return addOne
#     return counter(start)
#
# f = createCounter()
# print(f())
# print(f())
# print(f())
# print(f())
# print(f())

abs1 = abs
print(abs1.__name__)
