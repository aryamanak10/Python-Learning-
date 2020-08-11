# Class Methods and Class Attributes.

# Class Attribute - Attributes that are specific to the class but not the instance of the class.
class Person:

    #Class Attribute - Will not change from instance to instance, Defined for the entire class.
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        # Person.number_of_people += 1
        Person.add_person()

    # Class Method
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Hill")
# print(p1.number_of_people)

p2 = Person("Bill")
# print(p2.number_of_people)

# number_of_people is specific to the class and not the instance.
# print(Person.number_of_people)

# Person.number_of_people = 8
# print(p2.number_of_people)

# Person.number_of_people = 9
# print(p1.number_of_people)

print(Person.number_of_people_())