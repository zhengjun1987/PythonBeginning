# coding=utf-8
greetings = 'hello'
print greetings[0]  # h
print greetings[-1]  # o

# fourth = raw_input("Year:")[3]
# print fourth
#       Year:2008
#       8

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print bicycles  # ['trek', 'cannondale', 'redline', 'specialized']
print bicycles[0]  # trek
print bicycles[0].title()  # Trek
print bicycles[1]  # cannondale
print bicycles[3]  # specialized
print bicycles[-1]  # specialized

print "My first bike is a " + bicycles[0].title();  # My first bike is a Trek

motocycles = ['honda', 'yamaha', 'suzuki']
print motocycles  # ['honda', 'yamaha', 'suzuki']
motocycles[0] = 'ducati'  # ['ducati', 'yamaha', 'suzuki']
print motocycles

motocycles.append('ducati')
print motocycles  # ['ducati', 'yamaha', 'suzuki', 'ducati'] 列表元素内容可以重复

motocycles.insert(0, 'honda')
print motocycles  # ['honda', 'ducati', 'yamaha', 'suzuki', 'ducati']

del motocycles[0]
print motocycles  # ['ducati', 'yamaha', 'suzuki', 'ducati']

motocycles.__delitem__(1)
print motocycles  # ['ducati', 'suzuki', 'ducati']

pop = motocycles.pop()
print motocycles  # ['ducati', 'suzuki']
print pop  # ducati
# pop方法弹出的是按后进先出的规则弹出，stack栈

last_owned = motocycles.pop()
print "The last motocycle I owned is a " + last_owned + "."  # The last motocycle I owned is a suzuki.

print motocycles
motocycles.append('suzuki')
motocycles.append('honda')
motocycles.append('yamaha')
print motocycles
first_owned = motocycles.pop(0)
print "The first motocycle I owned is a " + first_owned + "."
print motocycles
# ['ducati', 'suzuki', 'honda', 'yamaha']
# The first motocycle I owned is a ducati.
# ['suzuki', 'honda', 'yamaha']

motocycles.append('honda')
print motocycles
# ['suzuki', 'honda', 'yamaha', 'honda']
remove = motocycles.remove('honda')
print remove
# None
print motocycles
# ['suzuki', 'yamaha', 'honda']

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print cars  # ['audi', 'bmw', 'subaru', 'toyota']
cars.sort(None, None, True)
print cars  # ['toyota', 'subaru', 'bmw', 'audi']

print "\nHere is a sorted list:"
print (sorted(cars))
print "\nHere is the original list:"
print (cars)
# Here is a sorted list:
# ['audi', 'bmw', 'subaru', 'toyota']
# Here is the original list:
# ['toyota', 'subaru', 'bmw', 'audi']

cars.reverse()
print cars  # ['audi', 'bmw', 'subaru', 'toyota']

length = len(cars)
print length  # 4

print cars[-1]  # toyota
cars.append("honda")
print cars[-1]  # honda
#
# cars = []
# print cars[-1]  # IndexError: list index out of range

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print magician.title() + ", that is a great trick!"
    print "I cannot wait to see your next trick," + magician.title()
print("Thank you, everyone. That was a great magic show!")

# Alice, that is a great trick!
# I cannot wait to see your next trick,Alice
# David, that is a great trick!
# I cannot wait to see your next trick,David
# Carolina, that is a great trick!
# I cannot wait to see your next trick,Carolina
# Thank you, everyone. That was a great magic show!

print magician.title()  # Carolina 脱离了for循环的循环单变量仍然保留了离开循环时最后的值

# print("Hello,Python world!") 将无需缩进的语句缩进的话会发生IndentationError: unexpected indent


for value in range(0, 100, 5):
    print value
    # range包前不包后

squares = []
for i in range(1,11):
    square = i**2
    squares.append(square)
print squares   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print min(squares)  # 1
print max(squares)  # 100
print sum(squares)  # 385

print min(bicycles) # cannondale
print max(bicycles) # trek
# print sum(bicycles)   #TypeError: unsupported operand type(s) for +: 'int' and 'str'

players = ['charles','martina','michael','florence','eli']
print players[1:4]  # ['martina', 'michael', 'florence']
print players[:4]  # ['charles', 'martina', 'michael', 'florence']
print players[1:]  # ['martina', 'michael', 'florence', 'eli']
print players[-3:]  # ['michael', 'florence', 'eli']

print "Here are first three players on my team:"
for player in players[:3]:
    print player.title()
# Here are first three players on my team:
# Charles
# Martina
# Michael

my_foods = ['falafel','pizza','carrot cake']
friend_foods = my_foods[:]
print my_foods  #  ['falafel', 'pizza', 'carrot cake']
print friend_foods  # ['falafel', 'pizza', 'carrot cake']
my_foods.append('cannoli')
friend_foods.append('ice cream')
print my_foods  # ['falafel', 'pizza', 'carrot cake', 'cannoli']
print friend_foods  # ['falafel', 'pizza', 'carrot cake', 'ice cream']


my_foods = ['falafel','pizza','carrot cake']
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print my_foods  # ['falafel', 'pizza', 'carrot cake', 'cannoli', 'ice cream']
print friend_foods  # ['falafel', 'pizza', 'carrot cake', 'cannoli', 'ice cream']

dimensions = (200,50)
print dimensions    #(200, 50)
print dimensions[0] #200
print dimensions[1] #50

for dimension in dimensions:
    print dimension
# 200
# 50

dimensions = (400,200)
print dimensions    #(400, 200)