'''
任何对象，只要正确实现了上下文管理，就可以用于with语句。
实现上下文管理是通过__enter__和__exit__这两个方法实现的。
'''
class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

with Query('Bob') as q:
    q.query()

from contextlib import contextmanager, closing
from urllib.request import urlopen


class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()

# 在某段代码执行前后自动执行特定代码
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

# 如果一个对象没有实现上下文，就不能把它用于with语句。可以用closing()来把该对象变为上下文对象
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

# closing也是一个经过@contextmanager装饰的generator
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
