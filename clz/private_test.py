
'''
鸭子类型
'''
class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):

    def run(self):
        print('Dog is running...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()


class Timer(object):
    def run(self):
        print('file-like object Start...')


class Student():
    def __init__(self, name, score):
        self.__name = name
        self._name1 = name
        self.__score = score
    def get_name(self):
        return self.__name
    def print_score(self):
        print("%s: %s" % (self.__name, self.__score))

'''
变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名

一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，
意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”

不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量.
强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
'''
if __name__ == '__main__':
    bart = Student('Bart Simpson', 59)
    bart._name1
    bart._Student__name
    #bart.__name

    bart.__name = 'New Name'
    print(bart.__name)
    print(bart.get_name())

    run_twice(Timer())

'''
外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。
'''
