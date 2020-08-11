# Object Oriented Programming in Python

class Dog:

    # init allows us to pass parameters when we first create an instance of our class.
    
    def __init__(self, name, age):

        # Created an attribute of the class dog which is 'name'.
        
        self.name = name
        self.age = age

    def add_one(self, x):
        return x + 1

    # Creating a method - Method is a function inside the class.
    # All the methods/functions start with a parameter called self.
    
    def bark(self):
        print("Bark")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

# Having a varible 'd' and going to assign it to an instance of the class Dog.
# __main__. is the module in which the class was defined in. Default value is 'main'.
# 'bark' is a method of the class dog. There can be many methods in the class.

d = Dog("Ronaldo", 35)
print(d.name)
print(d.get_name())
print(d.get_age())
d.set_age(23)
print(d.get_age())
d.bark()