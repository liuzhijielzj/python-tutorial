import json

d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    # 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可
    @staticmethod
    def student2dict(std):
        return {
            'name': std.name,
            'age': std.age,
            'score': std.score
        }

    @staticmethod
    def dict2student(d):
        return Student(d['name'], d['age'], d['score'])


s = Student('Bob', 20, 88)
json_str = json.dumps(s, default=Student.student2dict)
print(json_str)
# 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
print(json.dumps(s, default=lambda obj: obj.__dict__))
print(json.loads(json_str, object_hook=Student.dict2student))