#!/usr/bin/python
# -*- coding: UTF-8 -*-
import this
# number: int, long, float, complex
#不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象
a,b,c=1,2,3
print(a,b,c)
del a,b
print(c)

print(3 ** 3)

print(0.2 + 0.1)
print('i am ' + str(20) + ' years old') # can not use 'i am ' + 20 + ' years old'


#divide
print(10 / 2) #/除法计算结果是浮点数
print(10 // 3) # 3, 整数的地板除//永远是整数，即使除不尽。要做精确的除法，使用/就可以。
print(11.2 // 3) # 3.0

'''
Python的整数没有大小限制
Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）
'''