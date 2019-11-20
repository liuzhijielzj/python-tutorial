#!/usr/bin/python
# -*- coding: UTF-8 -*-

#List
list1 = [ 'runoob', 786 , 2.23, 'john', 70.2 ] # contains different data
tinylist = [123, 'john']
#加号 + 是列表连接运算符，星号 * 是重复操作
print(list1)
print(list1[::2]) # 2 is step
print(list1[0])
print(list1[:2])
print(list1[0:3])
print(list1[-5:-2]) # from right len + x
print(tinylist * 2)
print(tinylist + list1)

tinylist[0] = [222]
print(tinylist)
tinylist.append(2)
print(tinylist)
tinylist.insert(0, 0)
print(tinylist)
del tinylist[0]
print(tinylist)
tinylist.pop(1)
print(tinylist)
tinylist.append('x')
tinylist.append('x')
print(tinylist)
tinylist.remove('x') # only remove the first one
print(tinylist)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)
print(sorted(cars, reverse=True))

cars.sort(reverse=True)
print('cars after sorting:' + str(cars))

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
for car in cars:
    print(car)
    print("OK\n")

for n in range(1, 10):
    print(n)

evens = list(range(2, 11, 2))
print(evens)
print(min(evens))
print(max(evens))
print(sum((evens)))

squares = [value ** 2 for value in range(1, 11)]
print(squares)

for square in squares[1:5]:
    print(square)

nums = list(range(1, 100))
print(nums[::2])

print('ABCDEFG'[:3])

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in zip(range(1,len(L)+1),L):
    print(index, '-', name)