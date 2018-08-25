# coding=utf-8
print '"Hello,world",she said.'
print "Let's say "'"Hello,world!"'
# "Hello,world",she said.
# Let's say "Hello,world!"

print repr(10000L)
print repr("Hello,world!")
print str(10000L)
print str("Hello,world!")
# 10000L
# 'Hello,world!'
# 10000
# Hello,world!

temp = 42
print "The temperature is temp"  # The temperature is temp
print "The temperature is " + repr(temp)  # The temperature is 42
print "The temperature is " + str(temp)  # The temperature is 42
# print "The temperature is " + temp  # TypeError: cannot concatenate 'str' and 'int' objects
print "The temperature is " "temp"  # The temperature is temp
print "The temperature is " 'temp'  # The temperature is temp
print "The temperature is " + `temp`  # The temperature is 42
# 一对反引号中间放置变量名 等价于 repr()

# name = raw_input("What's your name?")
# print "Hello," + name + "!"
#       What's your name?Zheng Jun
#       Hello,Zheng Jun!

# name = input("What's your name?")
# print "Hello," + name + "!"
#       What's your name?"zhengjun"
#       Hello,zhengjun!

# raw_input和input方法的区别

print '''This is a very long string.
It continues here.
And it's not over yet.
"Hello,World!"
Still here.'''
# This is a very long string.
# It continues here.
# And it's not over yet.
# "Hello,World!"
# Still here.

print 'Hello\nworld!'
print 'http:\nowhere'
# Hello
# world!
# http:
# owhere

print r'Hello\nworld!'
print r'http:\nowhere'
# Hello\nworld!
# http:\nowhere