phonebook = {'Alice': '2341', 'Beth': '9102', 'Ceil': '3258'}
print dict([('name', 'Zheng Jun'), ('age', 42)])  # {'age': 42, 'name': 'Zheng Jun'}
print dict(name='zhengjun', age=42)  # {'age': 42, 'name': 'zhengjun'}

# x= []
# x[42]='Foobar' # IndexError: list assignment index out of range

x = {}
x[42] = 'Foobar'
print x[42]
print x

people = {
    'Alice':{'phone':'2314','addr':'Foo drive 23'},
    'Beth':{'phone':'2123','addr':'Foo drive 21'},
    'Ceil':{'phone':'4652','addr':'Foo drive 13'}
}

labels = {
    'phone':'Phone Number',
    'addr':'Address'
}

# name = raw_input("Name:")
# request = raw_input("Phone number(p) or Address(a)?")
# if request == 'p':
#     key = 'phone'
# elif request == 'a':
#     key = 'addr'
#
# if name in people:
#     print "%s\'s %s is %s" % (name,labels[key],people[name][key])
#
# Name:Alice
# Phone number(p) or Address(a)?a
# Alice's Address is Foo drive 23


