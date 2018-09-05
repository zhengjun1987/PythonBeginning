# -*- coding: utf-8 -*-
import copy

print 'Age', 42
print 1, 2, 3
print (1, 2, 3)

d = {'time': '2018年08月29日03:12:33', 'array': ['arr', '枕风宿雪多年', '我与虎谋早餐']}
deepcopy = copy.deepcopy(d)
print deepcopy

x, y, z = 1, 2, 3
print x, y, z
x, y = y, x
print x, y, z
x, y, z = (11, 22, 33)
print x, y, z
popitem = d.popitem()
print popitem
a, b = d.popitem()
print a, b

print True
print False
print True == 1
print False == 0
print True + False + 42
# True
# False
# True
# True
# 43

print bool('I think,therefore I am')
print bool(42)
print bool('')
print bool(0)
print bool(None)
# True
# True
# False
# False
# False

name = raw_input("What's your name?\n")
if (name.endswith('Gumby')):
    print 'Hello, Mr Gumby!'
else:
    print('Hello, stranger!')
# What's your name?
# Allen Gumby
# Hello, Mr Gumby!
