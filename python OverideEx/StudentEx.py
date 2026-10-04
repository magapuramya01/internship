class Student:
    def display(self):
        print("I am a student")


class GraduateStudent(Student):
    def display(self):
        print("I am a graduate student")


GraduateStudent().display()