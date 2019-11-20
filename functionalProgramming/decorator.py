'''
 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
 decorator就是一个返回函数的高阶函数。
 '''
def log(func):
    def wrapper(*args, **kw):
        print('Call %s():' % func.__name__)
        return func(*args, **kw) #此处必须原样使用*args,**kw
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

from functools import reduce
from time import time
def performance(f):
    def wrapper(*args, **kw):
        start = time()
        res = f(*args, **kw) # when invoke f, need to pass the arguments as (*args, **kw), not (args, kw)
        end = time()
        print('Call %s() in %fs' % (f.__name__, end - start))
        return res
    return wrapper

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

factorial(5)

from functools import reduce
import time
def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print('Call %s() in %f %s' % (f.__name__, t, unit))
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print(factorial(10))

def log(text = 'CALL'):
    def decorator(func):
        # @functools.wraps应该作用在返回的新函数上
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

# functools.partial可以把一个参数多的函数变成一个参数少的新函数，少的参数需要在创建时指定默认值
int2 = functools.partial(int, base=2)
print(int2('1000'))

from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True
print(func())
# Output: Function is running

can_run = False
print(func())
# Output: Function will not run

'''
装饰器能有助于检查某个人是否被授权去使用一个web应用的端点(endpoint)。它们被大量使用于Flask和Django web框架中。
'''
from functools import wraps

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    return decorated

#装饰器类
from functools import wraps

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass

class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''
    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        pass

@logit()
def myfunc1():
    pass
