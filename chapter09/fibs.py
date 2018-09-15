# FileName: chapter09/fibs.py
# Author:Zheng Jun
# Date:2018/9/15 10:37
# E-mail:zhengjun1987@outlook.com

class fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

f = fibs()
arr = []
for x in f:
    if x < 19999:
        arr.append(x)
    else:
        break

print(f"arr = {arr}")