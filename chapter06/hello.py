def hello(name):
    print(f"Hello, {name}!")


def hello1(greeting, name):
    print(f"{greeting}, {name}!")


def hello2(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


def print_params(*params):
    print(params)


def print_params2(title, *params):
    print(f"{title} : {params}")


def in_the_middle(title, *params, end):
    print(f"{title} : {params} ---- {end}")


def add(x, y):
    return x + y


params = 1, 2
print(add(*params))
# 3
params = {'greeting': 'Well met', 'name': 'Sir Robin'}
hello1(**params)
# Well met, Sir Robin!
hello2(**params)
# Well met, Sir Robin!
in_the_middle("Params", 1, 2, end=3)
# Params : (1, 2) ---- 3
print_params2("Params", 1, 2, 3)
# Params : (1, 2, 3)
print_params2("Nothing")
# Nothing : ()
print_params('Testing')
# ('Testing',)
print_params(1, 2, 3)
# (1, 2, 3)

hello1(name="Jun", greeting="Hi")
# Hi, Jun!
hello2("Jun")
hello2(greeting="Hi", name="Wolf")
hello2(name="Jun")
# Hello, Jun!
# Hello, Jun!

hello("World")
hello("Gumby")
# zhengjuns-MacBook-Pro:chapter06 zhengjun$ python3 hello.py
# Hello, World!
# Hello, Gumby!
