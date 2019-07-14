'''
 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
 decorator就是一个返回函数的高阶函数。
 '''
def log(func):
    def wrapper(*args, **kw):
        print('Call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2015-3-25')

# 等价log(now)
now()

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
def log(text):
    def decorator(func):
        # *args, **kw接受任意参数的调用
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

now()
#等价log('execute')(now)

#注意这里跟wrapper里面的func.__name__的区别
print(now.__name__)

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2017-3-25')

print(now.__name__)
now()
print(now.__name__)

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2017-3-25')

print(now.__name__)
now()
print(now.__name__)


def log(text = 'CALL'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin %s %s():' % (text, func.__name__))
            result = func(*args, **kw)
            print('end %s %s():' % (text, func.__name__))
            return result
        return wrapper
    return decorator

@log('EXECUTE')
def test():
    print('this is a test')

test()

int2 = functools.partial(int, base=2)
print(int2('1000'))
