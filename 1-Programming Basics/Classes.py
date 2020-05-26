# author: Allyson Vasquez
# version: May.26.2020
# Practice syntax and use of classes

class Student:
    def __init__(self, name, id, gpa):
        self.name = name
        self.id = id
        self.gpa = gpa

    def on_probation(self):
        if self.gpa <= 2.0:
            return bool(True)
        else:
            return bool(False)


student1 = Student('Allyson', 12345, 3.8)
student2 = Student('Bob', 54321, 1.7)

print(student1.name, student1.id, student1.gpa)
print('\tOn Probation:', student1.on_probation())

print(student2.name, student2.id, student2.gpa)
print('\tOn Probation:', student2.on_probation())

