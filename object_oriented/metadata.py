class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)
h = Hello()
h.hello()

print(type(Hello))
print(type(h))

def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)
Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass
L = MyList()
L.add(1)
print(L)