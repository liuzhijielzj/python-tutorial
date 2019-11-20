L = ['Adam', 'Lisa', 'Bart']
# in操作符跟JavaScript不同；这里就是遍历列表值，而JavaScript遍历数组索引
for name in L:
    print(name)
s = set(['Adam', 'Lisa', 'Bart', 'Paul'])
print('Bart' in s)

#key 的元素必须不可变,Python的基本类型如字符串、整数、浮点数都是不可变的，都可以作为 key。但是list是可变的，就不能作为 key。

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print(d)
# in操作符遍历dict索引
if 'Bart' in d:
    print(d['Bart'])
