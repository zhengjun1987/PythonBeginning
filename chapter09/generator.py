# FileName: chapter09/generator.py
# Author:Zheng Jun
# Date:2018/9/15 11:09
# E-mail:zhengjun1987@outlook.com

def flatten(nested):
    for secondarysequence in nested:
        if isinstance(secondarysequence, int):
            yield secondarysequence
        else:
            for x in secondarysequence:
                if isinstance(x, int):
                    yield x
                else:
                    for y in x:
                        if isinstance(y, int):
                            yield y


print(f"isinstance(6, int) = {isinstance(6, int)}")

print(f"list(flatten([[1, 2, 3], [4, [5, 6]], [7]])) = {list(flatten([[1, 2, 3], [4, [5, 6]], [7]]))}")
# zhengjuns-MacBook-Pro:chapter09 zhengjun$ python3 generator.py
# list(flatten([[1, 2, 3], [4, [5, 6]], [7]])) = [1, 2, 3, 4, [5, 6], 7]