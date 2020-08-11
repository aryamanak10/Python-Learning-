# Inheritance in Python

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")
    
    def speak(self):
        print("I don't know what I say.")

# Here in the parameters of the class we are give the class name from which the below class will "INHERIT".
# It is not write to "re-initialize" the name and age in the class Cat as it is already defined in the Pet Class. 
# Hence we use the super() which refers to the super/parent or the class inherited in the current class.

class Cat(Pet):
    
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}.")

class Dog(Pet):
    # def __init(self, name, age):
    #     self.name = name
    #     self.age = age
    
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.show()
p.speak()

c = Cat("Bill", 34, "Black")
c.show()
c.speak()

d = Dog("Joe", 24)
d.show()
d.speak()

f = Fish("Bubbles", 2)
f.speak()