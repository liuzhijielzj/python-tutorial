
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name


    '''
    直接显示变量调用的不是__str__()，而是__repr__()，
    两者的区别是__str__()返回用户看到的字符串，
    而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
    '''
    __repr__ = __str__

    '''
    写一个__getattr__()方法，动态返回一个属性
    
    当调用不存在的属性时, 调用__getattr__(self, 'score')
    
    返回函数也是完全可以的
    
    注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。
    '''
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

    '''
    任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
    
    __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
   
    如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。
    
    那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
    '''
    def __call__(self):
        print('My name is %s.' % self.name)

print(callable(Student('lzj')))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))


'''
一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    '''
    表现得像list那样按照下标取出元素，需要实现__getitem__()方法
    
    如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
    
    
    与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。

    定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口
    '''
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


# 要让 len() 函数工作正常，类必须提供一个特殊方法__len__()，它返回元素的个数
class Students(object):
    def __init__(self, *args):
        self.names = args
    def __len__(self):
        return len(self.names)
ss = Students('Bob', 'Alice', 'Tim')
print(len(ss))

'''
斐波那契数列是由 0, 1, 1, 2, 3, 5, 8…构成。
请编写一个Fib类，Fib(10)表示数列的前10个元素，print Fib(10) 
可以打印出数列的前 10 个元素，len(Fib(10))可以正确返回数列的个数10。
'''
class Fib(object):
    def __init__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        self.numbers = L

    def __str__(self):
        return str(self.numbers)

    __repr__ = __str__

    def __len__(self):
        return len(self.numbers)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

'''
p、q 都是整数，表示有理数 p/q。
'''
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    # 定义加法运算
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)
    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)
    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    # 类型转换为int
    def __int__(self):
        return self.p // self.q
    def __float__(self):
        return 1.0 * self.p / self.q
    def __str__(self):
        g = gcd(self.p, self.q)
        return '%s/%s' % (self.p / g, self.q / g)
    __repr__ = __str__

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print(r1 + r2)
print(int(r1))

