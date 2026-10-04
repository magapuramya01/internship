class Student:
    def introduce(self):
        print("I am a student")


class Employee:
    def introduce(self):
        print("I am an employee")


def introduce_person(obj):
    obj.introduce()


introduce_person(Student())
introduce_person(Employee())