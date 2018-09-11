#! /usr/bin/env python3

people = {
    'Alice': {'phone': '2341', 'addr': 'Foo drive 23'},
    'Beth': {'phone': '9102', 'addr': 'Bar street 42'},
    'Cecil': {'phone': '3158', 'addr': 'Baz avenue 90'},
    'Dick': {'phone': '9527'}
}

label = {
    'phone':"Phone Number",
    'addr':"Address"
}

name = input("Name:")

request = input("Phone number(p) or Address(a)?")

if request == 'p':key = 'phone'
if request == 'a':key = 'addr'

if name in people:print(f"{name}'s {label[key]} is {people.get(name,{}).get(key,'Not Available')}.")

# zhengjuns-MacBook-Pro:chapter04 zhengjun$ /Users/zhengjun/Desktop/PythonBeginning/chapter04/phone_book.py
# Name:Beth
# Phone number(p) or Address(a)?p
# Beth's Phone Number is 9102.
# zhengjuns-MacBook-Pro:chapter04 zhengjun$ /Users/zhengjun/Desktop/PythonBeginning/chapter04/phone_book.py
# Name:Cecil
# Phone number(p) or Address(a)?a
# Cecil's Address is Baz avenue 90.
# zhengjuns-MacBook-Pro:chapter04 zhengjun$ /Users/zhengjun/Desktop/PythonBeginning/chapter04/phone_book.py
# Name:Dick
# Phone number(p) or Address(a)?a
# Dick's Address is Not Available.
