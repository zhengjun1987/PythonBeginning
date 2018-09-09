# coding=utf-8
# x = 1
# while x <= 10:
#     print x
#     x += 1

# name = ''
# while not name:
#     name = raw_input("Please enter your name:\n")
# print "Hello,%s" % name
#
# Please enter your name:
#
# Please enter your name:
# Bill Gates
# Hello,Bill Gates

# words = ['This','is','an','ex','parrot']
# for word in words:
#     print word
#
# This
# is
# an
# ex
# parrot

# for num in range(1, 11):
#     print num
#
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# for char in "quick fox jumps over lazy dog":
#     print char

# d = {'x': 1, 'y': [1, 1], 'z': [1, 1, 1]}
# for key in d.keys():
#     print "%s => %s" % (key, d.get(key))
#
# y => [1, 1]
# x => 1
# z => [1, 1, 1]

# for k in d:
#     print "%s => %s" % (k, d.get(k))

# for k, v in d.items():
#     print "%s => %s" % (k, v)

names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
# for i in range(0, len(names)):
#     print names[i], 'is', ages[i]
#
# anne is 12
# beth is 45
# george is 32
# damon is 102

# dict = zip(names, ages)
# print dict
# for k in dict:
#     print "%s = > %s" % k
#
# [('anne', 12), ('beth', 45), ('george', 32), ('damon', 102)] 注意此处所得结果并非一个dictionary，而是一个元组的数组
# anne = > 12
# beth = > 45
# george = > 32
# damon = > 102
# from math import sqrt
#
# for n in range(99, 0, -1):
#     root = sqrt(n)
#     print n, ' => ', root, ' => ', int(root)
#     if root == int(root):
#         break
#
# 99  =>  9.94987437107  =>  9
# 98  =>  9.89949493661  =>  9
# 97  =>  9.8488578018  =>  9
# 96  =>  9.79795897113  =>  9
# 95  =>  9.74679434481  =>  9
# 94  =>  9.69535971483  =>  9
# 93  =>  9.64365076099  =>  9
# 92  =>  9.59166304663  =>  9
# 91  =>  9.53939201417  =>  9
# 90  =>  9.48683298051  =>  9
# 89  =>  9.43398113206  =>  9
# 88  =>  9.38083151965  =>  9
# 87  =>  9.32737905309  =>  9
# 86  =>  9.2736184955  =>  9
# 85  =>  9.21954445729  =>  9
# 84  =>  9.16515138991  =>  9
# 83  =>  9.11043357914  =>  9
# 82  =>  9.05538513814  =>  9
# 81  =>  9.0  =>  9


# word = raw_input("Please enter a word:\n")
# while word:
#     print "The word is ", word
#     word = raw_input("Please enter a word:\n")
#
# Please enter a word:
# first
# The word is  first
# Please enter a word:
# second
# The word is  second
# Please enter a word:
# third
# The word is  third
# Please enter a word:
#
#

# while "not empty":
#     word = raw_input("Please enter a word:\n")
#     if not word:
#         break
#     print "The word is ", word
#
# Please enter a word:
# first
# The word is  first
# Please enter a word:
# 2nd
# The word is  2nd
# Please enter a word:
# 3rd
# The word is  3rd
# Please enter a word:
#

# word = "not empty"
# while word:
#     word = raw_input("Please enter a word:\n")
#     if not word:
#         break
#     print "The word is ", word
# else:
#     print "No word input, bye!"
#
# Please enter a word:
# 1st
# The word is  1st
# Please enter a word:
# 2nd
# The word is  2nd
# Please enter a word:
#
#
# Process finished with exit code 0

# from math import sqrt
#
# for n in range(99, 80, -1):
#     root = sqrt(n)
#     print n, '--', root, '--', int(root)
#     if root == int(root):
#         print "Found!"
#         break
# else:
#     print "Not found!"  # for语句之后的else子句：for循环之中必须有break/return的使用，否则else语句是肯定会执行的
#
# 99 -- 9.94987437107 -- 9
# 98 -- 9.89949493661 -- 9
# 97 -- 9.8488578018 -- 9
# 96 -- 9.79795897113 -- 9
# 95 -- 9.74679434481 -- 9
# 94 -- 9.69535971483 -- 9
# 93 -- 9.64365076099 -- 9
# 92 -- 9.59166304663 -- 9
# 91 -- 9.53939201417 -- 9
# 90 -- 9.48683298051 -- 9
# 89 -- 9.43398113206 -- 9
# 88 -- 9.38083151965 -- 9
# 87 -- 9.32737905309 -- 9
# 86 -- 9.2736184955 -- 9
# 85 -- 9.21954445729 -- 9
# 84 -- 9.16515138991 -- 9
# 83 -- 9.11043357914 -- 9
# 82 -- 9.05538513814 -- 9
# Not found!
#
# print [x * x for x in range(1, 10)]  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# print '-' * 50
#
# print [(x, y) for x in range(3) for y in
#        range(3)]  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# ziped = zip(names, ages)
# print ziped
# [('anne', 12), ('beth', 45), ('george', 32), ('damon', 102)]
# print [(x, y) for x in names for y in ages]
# [('anne', 12), ('anne', 45), ('anne', 32), ('anne', 102), ('beth', 12), ('beth', 45), ('beth', 32), ('beth', 102),
#  ('george', 12), ('george', 45), ('george', 32), ('george', 102), ('damon', 12), ('damon', 45), ('damon', 32),
#  ('damon', 102)]
# print [(x, y) for x in names for y in ages if names.index(x) == ages.index(y)]
# [('anne', 12), ('beth', 45), ('george', 32), ('damon', 102)]
# 所以，zip()就等于[(x, y) for x in names for y in ages if names.index(x) == ages.index(y)]

# name = raw_input("Please enter your name:\n") or 'End!'
# if name == 'Ralph Auldus Melish':
#     print "Welcome!"
# elif name == 'Enid':
#     pass
# elif name == 'Bill Gates':
#     print "Denied!"
# elif name == 'Enid':
#     print "Denied!"
#
# Please enter your name:
# Enid
#
# Process finished with exit code 0

d = dict(zip(names, ages))
print d
x = d
print x
d = None
print x
x = None
print x
print d

x = d = dict(zip(names, ages))
del x
# print x # name 'x' is not defined
print d  # {'damon': 102, 'anne': 12, 'beth': 45, 'george': 32}
# 垃圾回收机制同Java，只要还存在指向栈内内存块的指针，就不会被回收
# del方法删除的只是变量名称（指针本身），无法删除指针指向的内存。
