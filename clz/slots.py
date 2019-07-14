from types import MethodType

class Student(object):
    __slots__ = ('name', 'age', 'score') # 用tuple定义允许绑定的属性名称

class Sub(Student):
    # __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    pass

def set_age(self, age):
    self.age = age

def set_score(self, score):
    self.score = score

# 所有实例都绑定方法，可以给class绑定方法
# 绑定的到底是static还是class方法？
Student.set_score = set_score

def main():
    s = Student()
    s.name = 'lzj'
    print(s.name)
    # 给实例绑定一个方法, 只对当前实例有效
    # s.set_age = MethodType(set_age, s)
    # s.set_age(10)
    s.set_score(120)
    sub = Sub()
    sub.extra = 20
    s.extra = 20

if __name__ == '__main__':
    main()