import logging

# debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用
logging.basicConfig(level=logging.INFO)

try:
    print(5/0)
except ZeroDivisionError as e:
    print("You can't divide by zero!")
    logging.info("this is a info message")
    logging.exception(e)

class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise # raise语句如果不带参数，就会把当前错误原样抛出

# bar()


def foo(s):
    n = int(s)
    # 启动Python解释器时可以用-O参数来关闭assert
    assert n != 0, 'n is zero!' # 如果断言失败，assert语句本身就会抛出AssertionError
    return 10 / n


def main():
    foo('0')

