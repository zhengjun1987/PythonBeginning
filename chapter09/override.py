# FileName: chapter09/override.py
# Author:Zheng Jun
# Date:2018/9/14 10:58
# E-mail:zhengjun1987@outlook.com

class A:
    def hello(self):
        print("Hello, I'm A")

class B(A):
    pass

a = A()
b = B()
a.hello()
b.hello()
# zhengjuns-MacBook-Pro:chapter09 zhengjun$ python3 override.py
# Hello, I'm A
# Hello, I'm A

class C(A):
    def hello(self):
        print("Hello, I'm C")

c = C()
c.hello()
# Hello, I'm C

class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("Aaaah...")
            self.hungry = False
        else:
            print("No, thanks!")


b = Bird()
b.eat()
# Aaaah...
b.eat()
# No, thanks!

class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squaak!'
    def sing(self):
        print(self.sound)

sb = SongBird()
sb.sing()
# Squaak!
sb.eat()
sb.eat()
# Traceback (most recent call last):
#   File "override.py", line 48, in <module>
#     sb.eat()
#   File "override.py", line 29, in eat
#     if self.hungry:
# AttributeError: 'SongBird' object has no attribute 'hungry'


# Aaaah...
# No, thanks!