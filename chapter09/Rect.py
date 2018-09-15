# FileName: chapter09/Rect.py
# Author:Zheng Jun
# Date:2018/9/15 09:55
# E-mail:zhengjun1987@outlook.com

class Rect:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, key, value):
        print(f"__setattr__ : (key, value) = {(key, value)}")
        if key == 'size':
            self.width, self.height = value
        else:
            # self.__dict__[key] = value
            super(Rect, self).__setattr__(key, value)

    def __getattr__(self, item):
        print(f"__getattr__ : item = {item}")
        if item == 'size':
            return self.width, self.height
        else:
            return self.__dict__[item]


r = Rect()
r.size = 150, 110
print(f"r.size = {r.size}")
r.squre = r.size[0] == r.size[1]
print(f"r.squre = {r.squre}")
