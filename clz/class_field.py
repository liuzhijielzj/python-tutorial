class Student(object):
    name = 'Student'

s = Student()
s.score = 90

print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name)
s.name = 'instance name'
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name)
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
