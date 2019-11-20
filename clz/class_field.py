class Student(object):
    name = 'Student' # 类属性

s = Student()
s.score = 90

print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name)
s.name = 'instance name'
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name)
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
#千万不要在实例上修改类属性，它实际上并没有修改类属性，而是给实例绑定了一个实例属性。

class Person(object):
    count = 0

    '''
    通过标记一个@classmethod，该方法将绑定到 Person 类上，而非类的实例。
    类方法的第一个参数将传入类本身，通常将参数名命名为cls。
    '''
    @classmethod
    def how_many(cls):
        return cls.count
    def __init__(self,name):
        self.name = name
        Person.count +=1

p1 = Person('Bob')
print(Person.count)

p2 = Person('Alice')
print(Person.count)

import types
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

p1 = Person('Bob', 90)
def retrieve_name(self):
    return self.name
p1.get_name = types.MethodType(retrieve_name, p1)
print(p1.get_name())

'''
直接把 lambda 函数赋值给 self.get_grade 和绑定方法有所不同，
函数调用不需要传入 self，但是方法调用需要传入 self。
'''
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'
    def get_score(self):
        return self.score

p1 = Person('Bob', 90)
print(p1.get_grade)
print(p1.get_score)
print(p1.get_grade())

