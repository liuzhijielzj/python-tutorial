'''
自省(introspection)，在计算机编程领域里，是指在运行时来判断一个对象的类型的能力。
它是Python的强项之一。Python中所有一切都是一个对象，而且我们可以仔细勘察那些对象。
Python还包含了许多内置函数和模块来帮助我们。
'''

# dir
# 返回一个列表，列出了一个对象所拥有的属性和方法
my_list = [1, 2, 3]
print(dir(my_list))

#如果我们运行dir()而不传入参数，那么它会返回当前作用域的所有名字。
test = 1
print(dir())

# type
# type函数返回一个对象的类型。
print(type(''))
# Output: <type 'str'>

print(type([]))
# Output: <type 'list'>

print(type({}))
# Output: <type 'dict'>

print(type(dict))
# Output: <type 'type'>

print(type(3))
# Output: <type 'int'>

# id()函数返回任意不同种类对象的唯一ID
name = "Yasoob"
print(id(name))

# inspect模块也提供了许多有用的函数，来获取活跃对象的信息
import inspect
print(inspect.getmembers(str))