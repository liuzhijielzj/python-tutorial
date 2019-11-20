from collections.abc import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

def findMaxAndMin(l):
    #return (max(l), min(l))
    if not l or len(l) < 1:
        return ()
    maxVal = l[0]
    minVal = l[0]
    for item in l:
        if item > maxVal:
            maxVal = item
        if item < minVal:
            minVal = item
    return (maxVal, minVal)

print(findMaxAndMin(None))
print(findMaxAndMin([]))
print(findMaxAndMin([1, 3, 2, 5, 3, 7, 3, 8, 9, 134., 2, -1]))

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

my_string = "Yasoob"
next(iter(my_string)) # iter根据一个可迭代对象返回一个迭代器对象
for s in my_string:
    print(s)