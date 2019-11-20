print(True and True)
print(False or True)
print(not True)
print(not None)
#None不能理解为0，因为0是有意义的，而None是一个特殊的空值

a = True
# 把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True
print(a and 'a=T' or 'a=F') # 返回的是'a=T'
# 布尔运算时，只要能提前确定计算结果，它就不会往后算了，直接返回结果。