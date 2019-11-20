class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        # print("Exception has been handled")
        self.file_obj.close()
        # return True

'''
1 with语句先暂存了File类的__exit__方法
2 然后它调用File类的__enter__方法
3 __enter__方法打开文件并返回给with语句
4 打开的文件句柄被传递给opened_file参数
5 我们使用.write()来写文件
6 with语句调用之前暂存的__exit__方法
7 __exit__方法关闭了文件

在第4步和第6步之间，如果发生异常，Python会将异常的type,value和traceback传递给__exit__方法。

当异常发生时，with语句会采取哪些步骤:
1. 它把异常的type,value和traceback传递给__exit__方法 
2. 它让__exit__方法来处理异常 
3. 如果__exit__返回的是True，那么这个异常就被优雅地处理了。 
4. 如果__exit__返回的是True以外的任何东西，那么这个异常将被with语句抛出。
'''
with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')
    opened_file.undefined_function()
