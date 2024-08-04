class Student:
    def __init__(self):
        self.course = None
        self.name = None

    def add_student(self):
        self.name = input("Enter Student Name: ")
        self.course = input("Enter Course Name: ")

    def show_student(self):
        print("NAME: ", self.name, "\nCourse ", self.course)


class Marks(Student):
    def __init__(self):
        self.total = None
        self.percentage = None

    def add_marks(self):
        self.add_student()
        a = int(input("Enter marks: "))
        b = int(input("Enter marks: "))
        c = int(input("Enter marks: "))
        self.total = (a+b+c)
        self.percentage = self.total / 3

    def show_marks(self):
        self.show_student()
        print("Total: ", self.total, "Percentage: ", self.percentage)


no = int(input("How many Student: "))
x = []
for i in range(no):
    i = Marks()
    i.add_marks()
    x.append(i)

for i in x:
    i.show_marks()
