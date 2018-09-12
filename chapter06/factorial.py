def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def combine(m, n):
    return factorial(m) // factorial(n) // factorial(m - n)


print(factorial(5))
print(combine(35, 20))
# zhengjuns-MacBook-Pro:chapter06 zhengjun$ python3 factorial.py
# 120
# 3247943160