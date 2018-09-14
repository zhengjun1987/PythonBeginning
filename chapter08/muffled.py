class MuffledCalculator:
    muffled = False
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print("Division by zero is illegal.")
            else:
                raise


calculator = MuffledCalculator()
print(f"calculator.calc('10 / 2') = {calculator.calc('10 / 2')}")
# calculator.calc('10 / 2') = 5.0
print(f"calculator.calc('10 / 0') = {calculator.calc('10 / 0')}")
# Traceback (most recent call last):
#   File "muffled.py", line 15, in <module>
#     print(f"calculator.calc('10 / 0') = {calculator.calc('10 / 0')}")
#   File "muffled.py", line 5, in calc
#     return eval(expr)
#   File "<string>", line 1, in <module>
# ZeroDivisionError: division by zero

calculator.muffled = True
print(f"calculator.calc('10 / 0') = {calculator.calc('10 / 0')}")
# Division by zero is illegal.
# calculator.calc('10 / 0') = None

