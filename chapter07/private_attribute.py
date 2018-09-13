class Secretive:
    def __inaccessible(self):
        print("Bet you cannot see me")

    def accessible(self):
        print("The secret message is : ")
        self.__inaccessible()

s = Secretive()

# s.__inaccessible()
# Traceback (most recent call last):
#   File "private_attribute.py", line 10, in <module>
#     s.__inaccessible()
# AttributeError: 'Secretive' object has no attribute '__inaccessible'

s.accessible()
# zhengjuns-MacBook-Pro:chapter07 zhengjun$ python3 private_attribute.py
# The secret message is :
# Bet you cannot see me

s._Secretive__inaccessible()
# zhengjuns-MacBook-Pro:chapter07 zhengjun$ python3 private_attribute.py
# Bet you cannot see me