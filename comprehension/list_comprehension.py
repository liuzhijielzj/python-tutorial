'''
It consists of
square brackets containing an expression followed by a for clause, then zero or more
for or if clauses. The expressions can be anything, meaning you can put in all kinds
of objects in lists. The result would be a new list made after the evaluation of the
expression in context of the if and for clauses.
'''
print([x * x for x in range(1, 11) if x % 2 == 0]) #for循环后面还可以加上if判断
print([m + n for m in 'ABC' for n in 'XYZ']) #可以使用两层循环
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

import os

print([d for d in os.listdir('.')])

print([s.lower() for s in ['1', 2, '3', '4', 5] if isinstance(s, str)])

s = {i * i for i in range(1, 10) if i % 2 == 0}
print(type(s))

dict_gok = {
    'name': 'lzj',
    'age': 18,
    'gender': 'Female'
}
d = {k: v for k, v in dict_gok.items()}
print(d)