#!/usr/bin/python
# -*- coding: UTF-8 -*-

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
if 'Bart' in d:
    print(d['Bart'])

# dictionary
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict['one'] )
print(dict[2])
print(tinydict)
print(tinydict.keys() )
print(tinydict.values())

for k, v in tinydict.items():
    print("key: " + k + ", value: " + str(v))

for k in sorted(tinydict.keys()):
    print(k)

values = set(tinydict.values())
print(values)

'''
避免key不存在的错误，有两种办法，
一是通过in判断key是否存在
二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
'''
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print( 'Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thomas', 100))

'''
正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象
这是因为dict根据key来计算value的存储位置，
如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
要保证hash的正确性，作为key的对象就不能变。
在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key
'''
key = [1, 2, 3]
d[key] = 'a list'