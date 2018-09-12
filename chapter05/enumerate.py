strings = ['ah', 'ok', 'yep', 'yes']
print(list(enumerate(strings)))
for index, string in enumerate(strings):
    print(f"{index} ---- {string}")

# zhengjuns-MacBook-Pro:chapter05 zhengjun$ python3 enumerate.py
# [(0, 'ah'), (1, 'ok'), (2, 'yep'), (3, 'yes')]
# 0 ---- ah
# 1 ---- ok
# 2 ---- yep
# 3 ---- yes
