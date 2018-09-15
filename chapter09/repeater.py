# FileName: chapter09/repeater.py
# Author:Zheng Jun
# Date:2018/9/15 12:25
# E-mail:zhengjun1987@outlook.com

def repeater(value):
    while True:
        yv = (yield value)
        print(f"repeater : value = {value}, yv = {yv}")
        if isinstance(yv, str):
            yv = yv.lower()
        if yv is not None: value += yv


r = repeater("HELLO,WORLD!")
print(f"r = {r}")
print(f"r.send(None) = {r.send(None)}")
print("==============")
# print(f"next(r) = {next(r)}")  # Return the next item from the iterator. If default is given and the iterator is exhausted, it is returned instead of raising StopIteration.
print(f"next(r) = {next(r)}")  # Return the next item from the iterator. If default is given and the iterator is exhausted, it is returned instead of raising StopIteration.
# zhengjuns-MacBook-Pro:chapter09 zhengjun$ python3 repeater.py
# next(r) = 42
# print(f"r.send('HELLO, PYTHON!') = {r.send('HELLO, PYTHON!')}")
# repeater : yv = hello, world!
print(f"next(r) = {next(r)}")
# repeater : yv = None
# next(r) = Hello, world!
counter = 0
while counter < 10:
    r.send(str(counter))
    print(f"next(r) = {next(r)}, counter = {counter}")
    counter += 1

def flatten(nested):
    for sub in nested:
        if isinstance(sub, list):
            for x in flatten(sub):
                yield x
        elif isinstance(sub, int):
            yield sub


f = flatten([1, [2, [3, [4, [5, [6, [7]]]]]]])
i = next(f)
while i is not None:
    print(f"i = {i}")
    i = next(f)