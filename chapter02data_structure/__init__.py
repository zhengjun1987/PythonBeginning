tag = '<a href="http://www.python.org">Python web Site</a>'
print tag[9:30]
# http://www.python.org
print tag[32:-4]
# Python web Site

# url = raw_input("Please enter the URL:")
# domin = url[11:-5]
# print "Domin name:" + domin
#       Please enter the URL:http://www.python.org
#       Domin name:python

numbers = range(1, 11, 1)
print numbers
print numbers[0:10:1]  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print numbers[0:10:2]  # [1, 3, 5, 7, 9]
print numbers[::4]  # [1, 5, 9]
print numbers[::-4]  # [10, 6, 2]
print numbers[::-1]  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# sentence = raw_input("Sentence:")
# text_width = len(sentence)
# box_width = text_width + 6
# screen_width = 80
# left_margin = (screen_width - box_width) // 2
# print
# print ' '*left_margin +'+'+ '-'*(box_width-2)+'+'
# print ' '*left_margin +'|'+ ' '*text_width+'|'
# print ' '*left_margin +'|'+ sentence+'|'
# print ' '*left_margin +'|'+ ' '*text_width+'|'
# print ' '*left_margin +'+'+ '-'*(box_width-2)+'+'
#
# Sentence:http://www.python.org
#
#                           +--------------------------+
#                           |                      |
#                           |http://www.python.org |
#                           |                      |
#                           +--------------------------+

permission = 'rw';
print 'r' in permission
print 'x' in permission

# users = ['min','foo','bar']
# name = raw_input("Enter your user name:")
# if name in users:
#     print 'OK!'
# else:
#     print 'Please check!'
#
# subject = '$$$ Get rich now! $$$'
# print '$$$' in subject
#
# Enter your user name:foo
# OK!
# True

# database = [
#     ['albert', '1234'],
#     ['dilber', '4242'],
#     ['smith', '1234'],
#     ['zhengjun', '1234']
# ]
# name = raw_input("User name:")
# password = raw_input("Password:")
# if [name, password] in database:
#     print "Access Granted!"
#
# User name:zhengjun
# Password:1234
# Access Granted!

nums = range(1, 1024, 2)
print min(nums)
# 1
print max(nums)
# 1023
print sum(nums)
# 262144
print len(nums)
# 512

print list('hello')  # ['h', 'e', 'l', 'l', 'o']

names = ['Alice', 'Barry', 'Cecil', 'Dee-Dee', 'earl'.title()]
print names
# ['Alice', 'Barry', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print names
# ['Alice', 'Barry', 'Dee-Dee', 'Earl']
names.remove('Alice')
print names
# ['Barry', 'Dee-Dee', 'Earl']


string = list('Perl')
print string
string[2:] = list('ar')
print string
string[1:] = list('ython')
print string

# ['P', 'e', 'r', 'l']
# ['P', 'e', 'a', 'r']
# ['P', 'y', 't', 'h', 'o', 'n']

numbers = [1, 5]
numbers[1:1] = range(2, 5)
print numbers  # [1, 2, 3, 4, 5]
numbers[1:4] = []
print numbers  # [1, 5]

lst = [1, 2, 3]
lst.append(4)
print lst  # [1, 2, 3, 4]

print list('hello').count('l')  # 2

x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print x.count(1)  # 2
print x.count([1, 2])  # 1

a = range(1, 4)
b = range(4, 7)
print a + b  # [1, 2, 3, 4, 5, 6]
print a  # [1, 2, 3]
a.extend(b)
print a  # [1, 2, 3, 4, 5, 6]

knights = ['we', 'are', 'the', 'knights', 'who', 'say', 'ni']
if 'we' in knights:
    print knights.index('we')  # 0
if 'who' in knights:
    print knights.index('who')  # 4
if 'herring' in knights:
    print knights.index('herring')

a.insert(3, 'four')
print a  # [1, 2, 3, 'four', 4, 5, 6]
a[3:5] = [4]
print a  # [1, 2, 3, 4, 5, 6]

pop = knights.pop()
print pop  # ni
print knights  # ['we', 'are', 'the', 'knights', 'who', 'say']
pop = knights.pop(0)
print pop  # we
print knights  # ['are', 'the', 'knights', 'who', 'say']

x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('to')
print x  # ['be', 'or', 'not', 'to', 'be']
del x[0]
print x  # ['or', 'not', 'to', 'be']

x.reverse()
print x  # ['be', 'to', 'not', 'or']

x.sort()
print x  # ['be', 'not', 'or', 'to']

print knights
print sorted(knights)
print knights
# ['are', 'the', 'knights', 'who', 'say']
# ['are', 'knights', 'say', 'the', 'who']
# ['are', 'the', 'knights', 'who', 'say']

print cmp(42, 32)  # 1
print cmp(42, 52)  # -1
print cmp(42, 42)  # 0

numbers = [5, 2, 9, 7]
numbers.sort(cmp)
print numbers  # [2, 5, 7, 9]

x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len)
print x  # ['add', 'acme', 'aerate', 'abalone', 'aardvark']
x.sort(key=len, reverse=True)
print x  # ['aardvark', 'abalone', 'aerate', 'acme', 'add']

print tuple([1, 2, 3]) #(1, 2, 3)
