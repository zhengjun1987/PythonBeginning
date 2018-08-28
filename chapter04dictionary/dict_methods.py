# coding=utf-8
d = {}
d['name'] = 'Gumby'
d['age'] = 42
print d
# {'age': 42, 'name': 'Gumby'}
print d.clear()
# None
print d
# {}


x = d
d['key'] = 'value'
print x
# {'key': 'value'}
d = {}
print x
# {'key': 'value'}

d = x
x.clear()
print d
# {}
# 此处将一个字典变量指向空字典不同于在该变量上调用clear方法



x = {'username': 'admin', 'machine': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machine'].remove('baz')
print x  # {'username': 'admin', 'machine': ['foo', 'bar']}
print y  # {'username': 'mlh', 'machine': ['foo', 'bar']}

import copy

d = {'names': ['Alfred', 'Betty']}
c = d.copy()
dc = copy.deepcopy(d)
d['names'].append('Clive')
print c  # {'names': ['Alfred', 'Betty', 'Clive']}
print dc  # {'names': ['Alfred', 'Betty']}

f = {}
fromkeys = f.fromkeys(x)
print f  # {}
print fromkeys  # {'username': None, 'machine': None}
print fromkeys.fromkeys(d)  # {'names': None}

f_fromkeys = f.fromkeys(x, '(Unknown)')
print f_fromkeys  # {'username': '(Unknown)', 'machine': '(Unknown)'}
f_fromkeys = f.fromkeys(['username', 'device'], '(Unknown)')
print f_fromkeys  # {'username': '(Unknown)', 'device': '(Unknown)'}

# print f_fromkeys['name']  # KeyError: 'name'
print f_fromkeys.get('name')  # None
print f_fromkeys.get('name','N/A')  # N/A
