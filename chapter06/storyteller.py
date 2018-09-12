def story(**kwds):
    # return "Once upon a time, there was a {job} called {name}.".format_map(kwds)
    return f"Once upon a time, there was a {kwds['job']} called {kwds['name']}."


def power(x, y, *others):
    if others:
        print(f"Received redundant parameters:{others}")
    return pow(x, y)


def interval(start, stop=None, step=1):
    """Imitates range for step > 0"""
    if stop is None:
        start, stop = 0, start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result


print(story(job='king', name='Gumby'))
print(story(name='Sir Robin', job='brave knight'))
params = {'job': 'language', 'name': 'Python'}
print(story(**params))
del params['job']
print(story(**params, job='stroke of genius'))
print(power(2, 3))
print(power(3, 2))
print(power(y=3, x=2))
params = (5,) * 2
print(power(*params))
print(power(3, 3, "Hello, World!"))
print(interval(10))
print(interval(1, 5))
print(interval(3, 12, 4))
l = interval(3, 7)
print(f"l = {l}")
print(power(*l))

# zhengjuns-MacBook-Pro:chapter06 zhengjun$ python3 storyteller.py
# Once upon a time, there was a king called Gumby.
# Once upon a time, there was a brave knight called Sir Robin.
# Once upon a time, there was a language called Python.
# Once upon a time, there was a stroke of genius called Python.
# 8
# 9
# 8
# 3125
# Received redundant parameters:('Hello, World!',)
# 27
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4]
# [3, 7, 11]
# l = [3, 4, 5, 6]
# Received redundant parameters:(5, 6)
# 81
