print(type(123))
print(type('str'))
print(type(None))
print(type(abs))

print(isinstance([1, 2, 3], (list, tuple)))

print(dir('abc'))

class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print(len(dog))

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
print(hasattr(obj, 'x'))
print(setattr(obj, 'x', 10))
print(getattr(obj, 'x'))
print(obj.x)
print(getattr(obj, 'y', 1))
