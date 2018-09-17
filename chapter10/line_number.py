# FileName: /Users/zhengjun/Desktop/PythonBeginning/chapter10/line_number.py #  1
# Author:Zheng Jun                                 #  2
# Date:2018/9/17 10:38                             #  3
# E-mail:zhengjun1987@outlook.com                  #  4
                                                   #  5
import fileinput                                   #  6
                                                   #  7
for line in fileinput.input(inplace=True):         #  8
    line = line.rstrip()                           #  9
    num = fileinput.lineno()                       # 10
    print(f"{line:<50} #{num:3d}")                 # 11
