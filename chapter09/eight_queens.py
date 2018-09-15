# FileName: /Users/zhengjun/Desktop/PythonBeginning/chapter09/eight_queens.py
# Author:Zheng Jun
# Date:2018/9/15 19:35
# E-mail:zhengjun1987@outlook.com
import random


def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens(num, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def prettyprint(solution):
    def line(pos, length=len(solution)):
        print(" · " * pos + " * " + " · " * (length - pos - 1))

    for pos in solution:
        line(pos)


# prettyprint(random.choice(list(queens(8))))
print(f"list(queens(4)) = {list(queens(4))}")
