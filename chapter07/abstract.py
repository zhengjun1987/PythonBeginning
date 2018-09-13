from abc import ABC, abstractmethod


class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass


# print(f"Talker() = {Talker()}")
# Traceback (most recent call last):
#   File "abstract.py", line 8, in <module>
#     print(f"Talker() = {Talker()}")
# TypeError: Can't instantiate abstract class Talker with abstract methods talk

class Knigget(Talker):
    def talk(self):
        print("Ni!")


k = Knigget()
print(f"isinstance(k, Talker) = {isinstance(k, Talker)}")


class Herring:
    def talk(self):
        print("Blubber")


h = Herring()
print(f"isinstance(h, Talker) = {isinstance(h, Talker)}")
# zhengjuns-MacBook-Pro:chapter07 zhengjun$ python3 abstract.py
# isinstance(k, Talker) = True
# isinstance(h, Talker) = False


Talker.register(Herring)
print(f"isinstance(h, Talker) = {isinstance(h, Talker)}")
print(f"issubclass(Herring, Talker) = {issubclass(Herring, Talker)}")
# isinstance(h, Talker) = True
# issubclass(Herring, Talker) = True

class Clam:
    pass


Talker.register(Clam)
c = Clam()
print(f"isinstance(c, Talker) = {isinstance(c, Talker)}")
print(f"issubclass(Clam, Talker) = {issubclass(Clam, Talker)}")
# isinstance(c, Talker) = True
# issubclass(Clam, Talker) = True
