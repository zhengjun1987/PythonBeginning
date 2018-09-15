# FileName: chapter09/arithmetric_sequence.py
# Author:Zheng Jun
# Date:2018/9/14 00:28
# E-mail:zhengjun1987@outlook.com

def check_index(key):
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        check_index(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        check_index(key)
        self.changed[key] = value


s = ArithmeticSequence(1, 2)
print(f"s[4] = {s[4]}")
s[4] = 2
print(f"s[4] = {s[4]}")
print(f"s[5] = {s[5]}")

del s[4]

# zhengjuns-MacBook-Pro:chapter09 zhengjun$ python3 arithmetric_sequence.py
# s[4] = 9
# s[4] = 2
# s[5] = 11
# Traceback (most recent call last):
#   File "arithmetric_sequence.py", line 32, in <module>
#     del s[4]
# AttributeError: __delitem__
# zhengjuns-MacBook-Pro:chapter0
