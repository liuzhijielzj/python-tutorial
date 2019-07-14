import  sys
print(sys.path)
sys.path.append('/Users/michael/my_py_scripts')


'''
设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。
设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。
'''