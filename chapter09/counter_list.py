class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, item):
        self.counter += 1
        return super(CounterList, self).__getitem__(item)


cl = CounterList(range(10))
print(f"cl = {cl}")
cl.reverse()
print(f"cl = {cl}")
del cl[3:6]
print(f"cl = {cl}")
print(f"cl.counter = {cl.counter}")
print(f"cl[4] + cl[2] = {cl[4] + cl[2]}")
print(f"cl.counter = {cl.counter}")
# zhengjuns-MacBook-Pro:chapter09 zhengjun$ python3 counter_list.py
# cl = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# cl = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# cl = [9, 8, 7, 3, 2, 1, 0]
# cl.counter = 0
# cl[4] + cl[2] = 9
# cl.counter = 2