#! /usr/bin/env python3

width = int(input("Please enter width:"))
price_width = 10
item_width = width - price_width
header_format = "{{:{}}}{{:>{}}}".format(item_width, price_width)
fmt = "{{:{}}}{{:{}.2f}}".format(item_width, price_width)
print("=" * width)
print(header_format.format("Item", "Price"))
print("-" * width)
print(fmt.format("Apples", 0.4))
print(fmt.format("Pears", 0.5))
print(fmt.format("Cantaloupes", 1.92))
print(fmt.format("Dried Apricots (16 oz.)", 8.00))
print(fmt.format("Prunes (4 lbs)", 12.00))
print("=" * width)
# zhengjuns-MacBook-Pro:chapter03 zhengjun$ /Users/zhengjun/Desktop/PythonBeginning/chapter03/price_list.py
# Please enter width:35
# ===================================
# Item                          Price
# -----------------------------------
# Apples                         0.40
# Pears                          0.50
# Cantaloupes                    1.92
# Dried Apricots (16 oz.)        8.00
# Prunes (4 lbs)                12.00
# ===================================
