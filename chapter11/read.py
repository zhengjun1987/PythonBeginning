# FileName: /Users/zhengjun/Desktop/PythonBeginning/chapter11/read.py
# Author:Zheng Jun
# Date:2018/9/18 09:08
# E-mail:zhengjun1987@outlook.com

f = open('../files/test.txt', 'r')
# for line in list(f.readlines()):
#     print(line, end='')
# print()
# zhengjuns-MacBook-Pro:chapter11 zhengjun$ python3 read.py
# Welcome to this file
# There is nothing here except
# This stupid haiku

# line = f.readline()
# while line is not None and len(line) > 0:
#     print(line, end='')
#     line = f.readline()
# print()
# zhengjuns-MacBook-Pro:chapter11 zhengjun$ python3 read.py
# Welcome to this file
# There is nothing here except
# This stupid haiku

# print(f"f.read() = {f.read()}")
# zhengjuns-MacBook-Pro:chapter11 zhengjun$ python3 read.py
# f.read() = Welcome to this file
# There is nothing here except
# This stupid haiku


# print(f"f.read(7) = {f.read(7)}")
# print(f"f.read(4) = {f.read(4)}")
# zhengjuns-MacBook-Pro:chapter11 zhengjun$ python3 read.py
# f.read(7) = Welcome
# f.read(4) =  to

f.close()