#!/usr/bin/python
# -*- coding: UTF-8 -*-

#元组不能二次赋值，相当于只读列表
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print(tuple)
print(tuple * 2)

# Error: tuple[1] = 1
for v in tuple:
    print(v)

'''
当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，
因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号
'''
t = (1)
print(t)
t=(1,)
print(t)

