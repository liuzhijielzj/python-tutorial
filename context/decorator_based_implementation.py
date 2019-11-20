from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()

with open_file('some_file') as f:
    f.write('hola!')

'''
1. Python解释器遇到了yield关键字。因为这个缘故它创建了一个生成器而不是一个普通的函数。 
2. 因为这个装饰器，contextmanager会被调用并传入函数名（open_file）作为参数。 
3. contextmanager函数返回一个以GeneratorContextManager对象封装过的生成器。
4. 这个GeneratorContextManager被赋值给open_file函数，我们实际上是在调用GeneratorContextManager对象。
'''