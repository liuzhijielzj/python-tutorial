class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    # 用装饰器函数把 get/set 方法“装饰”成属性调用
    @property
    def birth(self):
        return self._birth

    # 前一个@property装饰后的副产品
    @birth.setter
    def birth(self, value):
        self._birth = value

    # 只读“属性”。
    @property
    def age(self):
        return 2015 - self._birth

student = Student()
student.score = 100
student.birth = 1985
print(student.age)

