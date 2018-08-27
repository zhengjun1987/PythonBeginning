print 'With a moo-moo here, and a moo-moo there'.find('moo')
title = 'Monty Python\'s Flying Circus'
print title.find('Monty')
print title.find('Python')
print title.find('Flying')
print title.find('\'')
print title.find('Zirquss')

subject = '$$$Get rich now!!!$$$'
print subject.find('$$$')
print subject.find('$$$', 1)
print subject.find('!!!')
print subject.find('!!!', 0, 16)

seq = ['1', '2', '3', '4', '5']
print '+'.join(seq)
print '-'.join(seq)
print ''.join(seq)

print title.lower()
print title.upper()
print title
print title.istitle()
print title.islower()
print title.isupper()
print title.isalnum()
print title.isdigit()
print title.isalpha()

print title.swapcase()

print subject.replace('!!!', '...')

print '+'.join(seq).split('+')
print subject.split(' ')

print '     internal whitespaces were kept   '.strip()
print '*** SPAM*for*everyone!!!***'.strip(' *!')

from string import maketrans

table = maketrans('cs', 'kz')
print table
print len(table)
print maketrans('', '')[97:123]
print 'this is a terrible test'.translate(table)
print 'computer science constructs the frame of future'.translate(table)

# 7
# 0
# 6
# 15
# 12
# -1
# 0
# 18
# 15
# -1
# 1 + 2 + 3 + 4 + 5
# 1 - 2 - 3 - 4 - 5
# 12345
# monty
# python
# 's flying circus
# MONTY
# PYTHON
# 'S FLYING CIRCUS
# Monty
# Python
# 's Flying Circus
# False
# False
# False
# False
# False
# False
# mONTY
# pYTHON
# 'S fLYING cIRCUS
# $$$Get
# rich
# now...$$$
# ['1', '2', '3', '4', '5']
# ['$$$Get', 'rich', 'now!!!$$$']
# internal
# whitespaces
# were
# kept
# SPAM *
# for *everyone
#
#  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abkdefghijklmnopqrztuvwxyz{|}~��������������������������������������������������������������������������������������������������������������������������������
# 256
# abcdefghijklmnopqrstuvwxyz
# thiz
# iz
# a
# terrible
# tezt
# komputer
# zkienke
# konztruktz
# the
# frame
# of
# future
