# FileName: /Users/zhengjun/Desktop/PythonBeginning/chapter11/read_char.py
# Author:Zheng Jun
# Date:2018/9/18 10:07
# E-mail:zhengjun1987@outlook.com

filename = '../files/test.txt'


def process(string):
    print("Processing:", string)

# for line in open(filename):
#     process(line)

# with open(filename) as f:
#     for line in f:    # 此处不用调用f.readlines()
#         process(line)


# import fileinput
#
# for line in fileinput.input(filename):
#     process(line)

# with open(filename) as f:
#     for line in f.readlines():
#         process(line)
#
# with open(filename) as f:
#     for char in f.read():
#         process(char)
#
# with open(filename) as f:
#     while True:
#         line = f.readline()
#         if not line:
#             f.close()
#             break
#         process(line)
#
# with open(filename) as f:
#     char = f.read(1)
#     while char:
#         process(char)
#         char = f.read(1)
