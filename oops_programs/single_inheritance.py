class Student():
    def __init__(self):
        self.course = None
        self.name = None

    def add_student_details(self):
        self.name = input("Enter Student Name")
        self.course = input("Enter Course Name")

    def show_student(self):
        print("NAME: ", self.name, "Course ", self.course)


class Marks(Student):
    def __init__(self):
        self.total = None

    def add_marks(self):
        self.add_student_details()
        a = int(input("Enter marks: "))
        b = int(input("Enter marks: "))
        c = int(input("Enter marks: "))
        self.total = (a+b+c) / 3

    def show_marks(self):
        self.show_student()
        print(self.total)


s = Marks()
s.add_marks()
s.show_marks()
