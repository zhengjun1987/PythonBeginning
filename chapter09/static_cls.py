# FileName: chapter09/static_cls.py
# Author:Zheng Jun
# Date:2018/9/15 09:11
# E-mail:zhengjun1987@outlook.com

class MyClass:
    @staticmethod
    def smeth():
        print("This is a static method.")

    @classmethod
    def cmeth(cls):
        print("THis is a class method of ", cls)

mc = MyClass()
print(f"mc.smeth = {mc.smeth}")
# zhengjuns-MacBook-Pro:chapter09 zhengjun$ python3 static_cls.py
# mc.smeth = <function MyClass.smeth at 0x10053c268>  # 本质上是function不是method
print(f"mc.cmeth = {mc.cmeth}")
# mc.cmeth = <bound method MyClass.cmeth of <class '__main__.MyClass'>>
MyClass.smeth()
# This is a static method.
MyClass.cmeth()
# THis is a class method of  <class '__main__.MyClass'>
mc.cmeth()
# THis is a class method of  <class '__main__.MyClass'>
