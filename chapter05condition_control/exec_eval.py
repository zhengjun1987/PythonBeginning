from math import sqrt

exec "print \"Hello, World!\""
# Hello, World!

# exec "sqrt = 1"
# print sqrt(4) # TypeError: 'int' object is not callable

scope = {}
exec "sqrt = 3\nprint \"sqrt(inside scope) =\",sqrt" in scope
# sqrt(inside scope) = 3
print sqrt(4)
# 2.0

print scope['sqrt']  # 3

# result = eval(raw_input("Please enter an arithmetic expression:\n"))
# print "The result is", result
#
# Please enter an arithmetic expression:
# 6+18*2
# The result is 42
