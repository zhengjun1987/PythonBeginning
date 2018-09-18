# FileName: /Users/zhengjun/Desktop/PythonBeginning/chapter11/print_stdin.py
# Author:Zheng Jun
# Date:2018/9/18 10:33
# E-mail:zhengjun1987@outlook.com

import sys

f = open("../files/stdin.txt", "w")
for line in sys.stdin:
    print(line, file=f)

f.close()