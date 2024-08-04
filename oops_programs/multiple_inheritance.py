class Student:
    def __init__(self):
        self.name = None
        self.course = None

    def add_student(self):
        self.name = input("Enter Student name: ")
        self.course = input("Enter Course name: ")

    def show_student(self):
        print("Name: ", self.name, "Course: ",self.course )


class Marks:
    def __init__(self):
        self.total = None
        self.percentage = None

    def add_marks(self):
        self.a = int(input("Enter marks m1: "))
        self.b = int(input("Enter marks m2: "))
        self.c = int(input("Enter marks m3: "))

    def calculate(self):

        self.total = self.a + self.b + self.c
        self.percentage = self.total/3


class Result(Student, Marks):
    def add_details(self):
        self.add_student()
        self.add_marks()

    def show_marks(self):
        self.calculate()
        print("Total: ", self.total, "Percentage: ",self.percentage)


no = int(input("Enter How many Students: "))
x = []
for i in range(no):
    i = Result()
    i.add_details()
    x.append(i)

for i in x:
    i.show_marks()