name = ''
while not name.strip():
    name = input("Please enter your name:")
print(f"Hello, {name:>20}")
# zhengjuns-MacBook-Pro:chapter05 zhengjun$ python3 name.py
# Please enter your name:Michael Jackson
# Hello,      Michael Jackson
