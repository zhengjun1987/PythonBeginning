name = raw_input("What's your name?\n")
if(name.endswith('Gumby')):
    if(name.startswith('Mr.')):
        print "Hello, Mr. Gumby"
    elif(name.startswith('Mrs.')):
        print "Hello, Mrs. Gumby"
    else:
        print "Hello, Gumby"
else:
    print 'Hello,stranger!'
# What's your name?
# Mr.Jack Gumby
# Hello, Mr. Gumby