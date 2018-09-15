# FileName: chapter09/recursive_generator.py
# Author:Zheng Jun
# Date:2018/9/15 11:26
# E-mail:zhengjun1987@outlook.com

def flatten(nested, layer):
    print("  " * layer + f"flatten : nested = {nested}")
    try:  # 递归条件
        for sublist in nested:
            for x in flatten(sublist, layer + 1):
                print("  " * layer + f"x = {x}")
                yield x
    except TypeError:  # 基线条件
        print("  " * layer + f"nested = {nested}")
        yield nested


generator = flatten([1, [2, [3, [4, [5, [6, [7]]]]]]], 0)
print(f"generator = {generator}")
# print(f"list(flatten([[1, 2, 3], [4, [5, 6]], [7]])) = {list(generator)}")
# zhengjuns-MacBook-Pro:chapter09 zhengjun$ python3 recursive_generator.py
# list(flatten([[1, 2, 3], [4, [5, 6]], [7]])) = [1, 2, 3, 4, 5, 6, 7]

i = 0
while i < 7:
    print(f"next(generator) = {next(generator)}")
    i += 1
# zhengjuns-MacBook-Pro:chapter09 zhengjun$ python3 recursive_generator.py
# generator = <generator object flatten at 0x104e7c570>
# flatten : nested = [1, [2, [3, [4, [5, [6, [7]]]]]]]
#   flatten : nested = 1
#   nested = 1
# x = 1
# next(generator) = 1
#   flatten : nested = [2, [3, [4, [5, [6, [7]]]]]]
#     flatten : nested = 2
#     nested = 2
#   x = 2
# x = 2
# next(generator) = 2
#     flatten : nested = [3, [4, [5, [6, [7]]]]]
#       flatten : nested = 3
#       nested = 3
#     x = 3
#   x = 3
# x = 3
# next(generator) = 3
#       flatten : nested = [4, [5, [6, [7]]]]
#         flatten : nested = 4
#         nested = 4
#       x = 4
#     x = 4
#   x = 4
# x = 4
# next(generator) = 4
#         flatten : nested = [5, [6, [7]]]
#           flatten : nested = 5
#           nested = 5
#         x = 5
#       x = 5
#     x = 5
#   x = 5
# x = 5
# next(generator) = 5
#           flatten : nested = [6, [7]]
#             flatten : nested = 6
#             nested = 6
#           x = 6
#         x = 6
#       x = 6
#     x = 6
#   x = 6
# x = 6
# next(generator) = 6
#             flatten : nested = [7]
#               flatten : nested = 7
#               nested = 7
#             x = 7
#           x = 7
#         x = 7
#       x = 7
#     x = 7
#   x = 7
# x = 7
# next(generator) = 7

