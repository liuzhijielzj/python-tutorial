import functools

#利用total_ordering修饰器重载 ==, <=, > 运算符
@functools.total_ordering
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)
    __repr__ = __str__

    # 使用total_ordering修饰器重载 ==, <=, > 运算符
    def __eq__(self, other):
        return self.score == other.score

    def __le__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

students = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 77)]
print(sorted(students))
print(students)

def cmp(self, s):
    if self.score < s.score:
        return -1
    elif self.score > s.score:
        return 1
    else:
        return 0

print(sorted(students, key=functools.cmp_to_key(cmp)))
print(sorted(students, key=lambda s: s.score))
print(students)