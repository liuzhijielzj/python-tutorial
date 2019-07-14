from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(0, 0, 2)
print(isinstance(c, Circle)) # True
print(isinstance(c, tuple)) # True

