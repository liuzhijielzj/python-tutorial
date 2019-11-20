from collections import namedtuple
#一个命名元组(namedtuple)有两个必需的参数。它们是元组名称和字段名称。
'''
元组名称是Animal，字段名称是'name'，'age'和'type'。
namedtuple让你的元组变得自文档了。你只要看一眼就很容易理解代码是做什么的。
你也不必使用整数索引来访问一个命名元组，这让你的代码更易于维护。
而且，namedtuple的每个实例没有对象字典，所以它们很轻量，与普通的元组比，并不需要更多的内存。这使得它们比字典更快。
'''
Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print(perry)
## 输出: Animal(name='perry', age=31, type='cat')

print(perry.name)
print(perry[0])
print(perry._asdict())


