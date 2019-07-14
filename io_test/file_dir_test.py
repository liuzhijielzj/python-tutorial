import os

# 操作文件和目录的函数一部分放在os模块，一部分放在os.path模块

print(os.name)
print(os.environ)
print(os.environ.get('path'))
print(os.environ.get('x', 'default'))
print(os.path.abspath('.'))
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
os.path.join('E:\\code\\file', 'testdir')
os.mkdir('E:\\code\\file\\testdir')
# ('E:\\code\\file', 'alice.text')
print(os.path.split('E:\\code\\file\\alice.text'))
# ('E:\\code\\file\\alice', '.text')
print(os.path.splitext('E:\\code\\file\\alice.text'))
os.rmdir('E:\\code\\file\\testdir')

print([x for x in os.listdir('.') if os.path.isdir(x)])
print( [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

os.rename('test.txt', 'test.py')
