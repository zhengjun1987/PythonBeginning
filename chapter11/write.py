# FileName: /Users/zhengjun/Desktop/PythonBeginning/chapter11/write.py
# Author:Zheng Jun
# Date:2018/9/18 09:57
# E-mail:zhengjun1987@outlook.com

f = open('../files/test.txt')
lines = f.readlines()
f.close()
lines[1] = "isn't a\n"
f = open('../files/test.txt', 'w')
f.writelines(lines)
# this
# isn't a
# haiku

# f.write("this\nis no\nhaiku")
# this
# is no
# haiku
f.close()