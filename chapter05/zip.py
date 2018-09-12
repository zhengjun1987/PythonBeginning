names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old.")
# zhengjuns-MacBook-Pro:chapter05 zhengjun$ python3 zip.py
# anne is 12 years old.
# beth is 45 years old.
# george is 32 years old.
# damon is 102 years old.

print(list(zip(names, ages)))
# [('anne', 12), ('beth', 45), ('george', 32), ('damon', 102)]
print(zip(names, ages))  # <zip object at 0x101a548c8>
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
# anne is 12 years old.
# beth is 45 years old.
# george is 32 years old.
# damon is 102 years old.