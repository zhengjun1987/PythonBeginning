# FileName: chapter09/constructor.py
# Author:Zheng Jun
# Date:2018/9/14 10:47
# E-mail:zhengjun1987@outlook.com

class FooBar:
    def __init__(self, v: object = 42) -> object:
        self.somevar = v


f = FooBar()
print(f"f.somevar = {f.somevar}")
f = FooBar("This is a constructor argument")
print(f"f.somevar = {f.somevar}")
# zhengjuns-MacBook-Pro:chapter09 zhengjun$ python3 constructor.py
# f.somevar = 42
# f.somevar = This is a constructor argument