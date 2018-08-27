format1 = 'Hello,%s,%s for ya?'
values = ('Helen', 'Hot')
print format1 % values  # Hello,Helen,Hot for ya?

format1 = "Pi with 3 decimals:%.3f"
from math import pi

print format1 % pi  # Pi with 3 decimals:3.142

print '%s plus %s equals %s' % (1, 1, 2)  # 1 plus 1 equals 2
# print '%s plus %s equals %s' % [1,1,2]#  TypeError: not enough arguments for format string

# width = input("Please enter the width:")
# price_width = 10
# item_width = width - price_width
# header_format = '%-*s%*s'
# format1 = '%-*s%*.2f'
# print '='*width
# print header_format%(item_width,'Item',price_width,'Price')
# print '-'*width
# print format1 % (item_width,'Apples',price_width,0.4)
# print format1 % (item_width,'Pears',price_width,0.5)
# print format1 % (item_width,'Cantaloupes',price_width,1.92)
# print format1 % (item_width,'Dried Apricots(16 oz)',price_width,8)
# print format1 % (item_width,'Prunes(4lbs)',price_width,12)
# print '='*width
#
# Please enter the width:40
# ========================================
# Item                               Price
# ----------------------------------------
# Apples                              0.40
# Pears                               0.50
# Cantaloupes                         1.92
# Dried Apricots(16 oz)               8.00
# Prunes(4lbs)                       12.00
# ========================================

f_pi = '%5.3f' % pi
print f_pi
print len(f_pi)