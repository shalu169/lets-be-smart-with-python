'''
# making a class
class Dog:   # generally use camel case
    pass
'''
# each dog has different name and age but all ara mammal.


class Dog:
    species = 'mammal'  # class attribute  (will be for all instances

    # initializer/instance attribute
    def __init__(self, name, age):    # we need not to call this function. yhis will automatically be called once an instance will be created.
        self.name = name
        self.age = age
    # instance method: Instance methods are defined inside a class and are used to get the contents of an instance.

    def description(self):
        print("this {} dog is {} years old".format(self.name, self.age))
    def sound(self, sound):
        return "this {} dog has {} sound".format(self.name, sound)


# Instantiate the Dog object


filo = Dog("filo", 5)
mikey = Dog("Mikey", 6)
print("{} is {} and type {} and {} is {} and type {}".format(filo.name, filo.age, filo.species, mikey.name, mikey.age, mikey.species))
william = Dog("William", 9)

# function to find biggest one
def big_one(*args):
    return max(args)

print("the oldest dog is {}".format(big_one(filo.age,mikey.age,william.age)))
mikey.description()
print(mikey.sound("buzz buzz"))
# modifying class attribute
class Email:
    def __init__(self):
        self.is_sent = False
    def send_email(self):
        self.is_sent = True


new_mail = Email()
print(new_mail.is_sent)
new_mail.send_email()
print(new_mail.is_sent)

# python object inheritance
#Dog Park Example
'''
class Dog:
    def __init__(self, breed):
        self.breed = breed
spencer = Dog('German Shepard')
sara = Dog("Boston Terrier")
print(sara.breed)
print(spencer.breed)
'''

# lets consider this individual breed have its own property
# lets make separate class for each breed

class Dog1:
    species = 'mammels'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print("this {} dog is {} years old".format(self.name, self.age))

    def sound(self, sound):
        return "this {} dog has {} sound".format(self.name, sound)

# child class inherit from Dog1 class


class RussellTerrier(Dog1):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed )
# Child class (inherits from Dog class)


class Bulldog(Dog1):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
# Child classes inherit attributes and
# behaviors from the parent class

jim = Bulldog("Jim", 12)
jim.description()

# Child classes have specific attributes
# and behaviors as well
print(jim.run("slowly"))

# we did not add individual attributes to each sub class

# Is jim an instance of Dog()?
print(isinstance(jim, Dog1))

# Is julie an instance of Dog1()?
julie = Dog1("Julie", 100)
print(isinstance(julie, Dog1))

# Is johnny walker an instance of Bulldog()
johnnywalker = RussellTerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))

# Is julie and instance of jim?
# print(isinstance(julie, jim)) # TypeError: isinstance() arg 2 must be a class, type, or tuple of classes and types


# Overriding the Functionality of a Parent Class
# Remember that child classes can also override attributes and behaviors from the parent class.

class Dog2:
    species = 'mammal'
class SomeBreed(Dog2):
    pass
class SomeOtherBreed(Dog2):
    species = 'reptile'  # overriding
frank = SomeBreed()
print(frank.species)
beans = SomeOtherBreed()
print(beans.species)