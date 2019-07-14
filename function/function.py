'''函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”'''
a = abs
print(abs(3.5))

def nop():
    pass

'''数据类型检查可以用内置函数isinstance()实现'''
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError()

import math

'''
返回多个值
返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值
'''
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

def quadratic(a, b, c):
    answer1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    answer2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    return answer1, answer2

print(quadratic(4, 15, 2))


'''
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
定义默认参数要牢记一点：默认参数必须指向不变对象！

'''
def add_end(L=[]):
    L.append('END')
    return L

print(add_end())
print(add_end())
print(add_end())

'''
可变参数函数
'''
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc())
print(calc(1, 2, 3))
nums = [1, 2, 3, 4]
print(calc(*nums))

'''
关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
'''
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
print(person('Michael', 30))
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
pro = {'city': 'Beijing', 'job': 'Engineer'}
person('Tom', 30, **pro)
'''
要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数
关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
'''
def person(name, age, *, city, job):
    print(name, age, city, job)
print(person('Jack', 24, city='Beijing', job='Engineer'))
print(person('Zhijie Liu', 32, city='Changsha', job='Teacher'))

'''
如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
'''
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

'''
命名关键字参数可以有缺省值，从而简化调用
'''
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person('Zhijie Liu', 32, job='Teacher')


'''
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
'''
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1, 2)
f1(1, 2, 3)
f1(1, 2, c = 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

'''
最神奇的是通过一个tuple和dict，你也可以调用上述函数
对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
'''
args = (1, 2, 3)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)


'''
解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，
使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
'''


def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)



def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('harry', 'hamster', ) # positional argument
describe_pet(animal_type='hamster', pet_name='harry') # keyword argument

describe_pet('harry') # default value

def makePizza(*topping):
    '''print topping '''
    print(topping)
makePizza('a', 'b')
makePizza()

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
user_profile = build_profile('albert', 'einstein', user_info = {'location' : 'princeton', 'field' : 'physics'})
print(user_profile)
