cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print car.upper()
    else:
        print car.title()
# Audi
# BMW
# Subaru
# Toyota

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print "Hold the anchovies!"
# Hold the anchovies!

answer = 42
print answer > 18
print answer < 25
print 19 < answer < 48
print answer > 18 and answer != 45

age0 = 22
age1 = 18
print age0 >= 21 and age1 >= 21
age1 = 22
print age0 >= 21 and age1 >= 21

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print 'onions' in requested_toppings
print 'pepperoni' in requested_toppings

if 'carrot' not in requested_toppings:
    print "Please check the request list!"

game_active = True
can_edit = False
car = 'subaru'
print ("car == 'subaru'? I predict true")
print car == 'subaru'
# car == 'subaru'? I predict true
# True