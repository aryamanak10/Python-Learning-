# Object Oriented Programming in Python

class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age

        # 0 - 100 marks
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students

        # .students is an attribute and not a method as it is not defined in the __init__ function.
        self.students = []

    # The parameter student in the below function is an instance of the Student object.
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        
        return False
    
    def get_average_grade(self):
        
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value/len(self.students)

# Adding a method which will allow us to add the Students in the Course.

s1 = Student("Aryu", 19, 95)
s2 = Student("Bill", 20, 24)
s3 = Student("Jill", 23, 14)

course = Course("Computers", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

# Both the elements inside our list are Student objects.
print(course.students[0].name)
print(course.add_student(s3))
print(course.get_average_grade())