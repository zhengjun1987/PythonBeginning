print 'foo' == 'foo'
print 'foo' == 'bar'
# True
# False

x = y = [1, 2, 3]
z = [1, 2, 3]
print x == y
print x == z
print y == z
print x is y
print x is z
print y is z
# True
# True
# True
# True
# False
# False

y = [2, 4]
print x is not y
del (x[2])
y[1] = 1
y.reverse()
print x
print y
print x == y
print x is y
# True
# [1, 2]
# [1, 2]
# True
# False

print 's' in 'Windows'
print 'dows' in 'Windows'
# True
# True

print 'alpha' < 'beta'
print 'FnOrD'.lower() == 'Fnord'.lower()
print [1, 2] < [2, 1]
print [2, [1, 4]] < [2, [1, 5]]
# True
# True
# True
# True
