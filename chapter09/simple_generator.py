# FileName: chapter09/simple_generator.py
# Author:Zheng Jun
# Date:2018/9/15 12:19
# E-mail:zhengjun1987@outlook.com

def simple_generator():
    yield 1
    print("Here the next value active")

print(f"simple_generator = {simple_generator}")
print(f"simple_generator() = {simple_generator()}")
# zhengjuns-MacBook-Pro:chapter09 zhengjun$ python3 simple_generator.py
# simple_generator = <function simple_generator at 0x1034ab400>
# simple_generator() = <generator object simple_generator at 0x103526570>