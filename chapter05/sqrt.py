from math import sqrt

for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Didn't find it!")
# zhengjuns-MacBook-Pro:chapter05 zhengjun$ python3 sqrt.py
# 81
