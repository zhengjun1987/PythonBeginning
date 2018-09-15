# FileName: chapter09/rectangle.py
# Author:Zheng Jun
# Date:2018/9/15 08:28
# E-mail:zhengjun1987@outlook.com

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    size = property(get_size, set_size)


r = Rectangle()
r.width = 10
r.height = 5
print(f"r.get_size() = {r.get_size()}")
# zhengjuns-MacBook-Pro:chapter09 zhengjun$ python3 rectangle.py
# r.get_size() = (10, 5)
# r.set_size(150, 100)
r.size = 150, 100
print(f"r.width = {r.width}")
# r.width = 150
print(f"r.size = {r.size}")
# r.size = (150, 100)