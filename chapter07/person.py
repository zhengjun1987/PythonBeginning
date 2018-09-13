class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print(f"Hello, world! I'm {self.name}.")


foo = Person()
bar = Person()
foo.set_name("Luke Skywalker")
bar.set_name("Anakin Skywalker")
foo.greet()  # Hello, world! I'm Luke Skywalker.
bar.greet()  # Hello, world! I'm Anakin Skywalker.


class Class:
    def method(self):
        print(f"I have a self:{self}")

    @staticmethod
    def function():
        print("I don't ...")


def function1():
    print("I don't ...")


instance = Class()
instance.method()
# I have a self:<__main__.Class object at 0x10ae37828>
Class.function()
# I don't ...
instance.method = function1
instance.method()


# I don't ...


class Bird:
    song = "Squaawk!"

    def sing(self):
        print(self.song)


bird = Bird()
bird.sing()  # Squaawk!
birdsong = bird.sing
birdsong()  # Squaawk!