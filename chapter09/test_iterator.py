# FileName: chapter09/test_iterator.py
# Author:Zheng Jun
# Date:2018/9/15 10:50
# E-mail:zhengjun1987@outlook.com

class TestIterator:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
        self.next = self.start - self.step

    def __iter__(self):
        return self

    def __next__(self):
        self.next += self.step
        if self.next < self.end:
            return self.next
        else:
            raise StopIteration

ti = TestIterator(0,100,3)
print(f"list(ti) = {list(ti)}")
# zhengjuns-MacBook-Pro:chapter09 zhengjun$ python3 test_iterator.py
# list(ti) = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]