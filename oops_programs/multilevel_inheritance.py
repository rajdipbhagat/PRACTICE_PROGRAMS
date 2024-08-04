class Student:
    def __init__(self):
        self.name = None
        self.course = None

    def add_student(self):
        self.name = input("Enter Student Name: ")
        self.course = input("Enter Student Course: ")

    def show_student(self):
        print("Name: ", self.name, "  ", "\nCourse: ", self.course)


class Marks(Student):
    def add_marks(self):
        self.add_student()
        self.a = int(input("Enter marks m1: "))
        self.b = int(input("Enter marks m2: "))
        self.c = int(input("Enter marks m3: "))

    def show_marks(self):
        self.show_student()
        print("Marks = ", self.a, " ", self.b, " ", self.c)


class Result(Marks):
    def add_details(self):
        self.add_marks()
        self.total = (self.a + self.b + self.c)
        self.percentage = self.total/3

    def show_details(self):
        self.show_marks()
        print("Total: ", self.total," ", "\nPercentage: ", self.percentage )


no = int(input("Enter How many Students: "))
x = []
for i in range(no):
    i = Result()
    i.add_details()
    x.append(i)

for i in x:
    i.show_details()

