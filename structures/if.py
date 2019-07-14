#!/usr/bin/python
# -*- coding: UTF-8 -*-

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if 'bmw' == car:
        print(car.upper())
    elif 'audi' == car:
        print(car.lower())
    else:
        print(car.title())

if cars: #list not empty
    print('we have cars')

if 'bmw' in cars:
    print('we have bmw')

age0 = 1
age1 = 30
if age0 > 0 and age1 < 50:
    print("still young!")

if age0 < 0 or age1 >= 50:
        print("not young!")

'''只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False'''
x=True
if x:
    print('True')