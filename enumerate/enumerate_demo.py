# 允许我们遍历数据并自动计数
some_list = [i ** 2 for i in range(10)]
for counter, value in enumerate(some_list):
    print(counter, value)

# enumerate也接受一些可选参数
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1): # 可选参数允许我们定制从哪个数字开始枚举
    print(c, value)

# 用来创建包含索引的元组列表
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list) # [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]
