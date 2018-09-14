try:
    x = int(input("Enter the first number:"))
    y = int(input("Enter the second number:"))
    print(f"x / y = {x / y}")
except (NameError, ZeroDivisionError) as e:  # 指定的异常发生时执行此代码块
    print(f"e = {e}")
    print("Your numbers were bogus...")
except:  # 除了指定之外的异常发生时执行此代码块
    print("Something wrong happened.")
else:  # 一切正常，没有异常发生时执行此代码块
    print("Ah, everything is fine!")
finally:  # 最终执行此代码块
    print("It's the end.")
# except ZeroDivisionError:
#     print("The second number cannot be zero.")
# except ValueError:
#     print("That wasn't a number, was it?")

# zhengjuns-MacBook-Pro:chapter08 zhengjun$ python3 division.py
# Enter the first number:10
# Enter the second number:0
# Traceback (most recent call last):
#   File "division.py", line 3, in <module>
#     print(f"x / y = {x / y}")
# ZeroDivisionError: division by zero

# zhengjuns-MacBook-Pro:chapter08 zhengjun$ python3 division.py
# Enter the first number:10
# Enter the second number:0
# The second number cannot be zero.

# zhengjuns-MacBook-Pro:chapter08 zhengjun$ python3 division.py
# Enter the first number:10
# Enter the second number:one
# That wasn't a number, was it?

# zhengjuns-MacBook-Pro:chapter08 zhengjun$ python3 division.py
# Enter the first number:10
# Enter the second number:0
# e = division by zero
# Your numbers were bogus...
# zhengjuns-MacBook-Pro:chapter08 zhengjun$ python3 division.py
# Enter the first number:19
# Enter the second number:two
# e = invalid literal for int() with base 10: 'two'
# Your numbers were bogus...
