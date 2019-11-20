from collections import defaultdict
import json

# 不需要检查key是否存在
colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)

# 当你在一个字典中对一个键进行嵌套赋值时，如果这个键不存在，会触发keyError异常。
#  defaultdict允许我们用一个聪明的方式绕过这个问题。
# some_dict = {}
# some_dict['colours']['favourite'] = "yellow"

tree = lambda: defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"

print(json.dumps(some_dict))

'''
defaultdict接受一个工厂函数作为参数.
这个factory_function可以是list、set、str等等，作用是当key不存在时，返回的是工厂函数的默认值，
比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0
'''
dict1 = defaultdict(int)
dict2 = defaultdict(set)
dict3 = defaultdict(str)
dict4 = defaultdict(list)
dict1[2] ='two'

print(dict1[1])
print(dict2[1])
print(dict3[1])
print(dict4[1])