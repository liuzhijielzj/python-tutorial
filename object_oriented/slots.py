class Student(object):
    __slots__ = ('name', 'age', 'score', 'set_age')  # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Michael'
print(s.name)
def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

def set_score(self, score):
    self.score = score

Student.set_score = set_score
s.set_score(100)
print(s.score)

# 绑定属性'gender'
#s.gender = 'M'

#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
    __slots__ = ('gender')

g = GraduateStudent()
g.name = 'g'
g.gender = 'M'
g.gender1 = 'M'



