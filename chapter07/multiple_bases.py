class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print("Hi my value is", self.value)


class TalkingCalculator(Calculator, Talker):
    pass


tc = TalkingCalculator()
tc.calculate("1 + 2 * 3")
tc.talk()
# zhengjuns-MacBook-Pro:chapter07 zhengjun$ python3 multiple_bases.py
# Hi my value is 7

print(f"hasattr(tc, 'talk') = {hasattr(tc, 'talk')}")
# hasattr(tc, 'talk') = True
print(f"hasattr(tc, 'value') = {hasattr(tc, 'value')}")
# hasattr(tc, 'value') = True
print(f"hasattr(tc, 'calculate') = {hasattr(tc, 'calculate')}")
# hasattr(tc, 'calculate') = True
print(f"hasattr(tc, 'fnord') = {hasattr(tc, 'fnord')}")
# hasattr(tc, 'fnord') = False
print(f"hasattr(tc,'__str__') = {hasattr(tc,'__str__')}")
# hasattr(tc,'__str__') = True

print(f"callable(getattr(tc,'talk', None)) = {callable(getattr(tc,'talk', None))}")
# callable(getattr(tc,'talk', None)) = True
print(f"callable(getattr(tc, 'fnord', None)) = {callable(getattr(tc, 'fnord', None))}")
# callable(getattr(tc, 'fnord', None)) = False

print(f"tc.__dict__ = {tc.__dict__}")   # tc.__dict__ = {'value': 7}