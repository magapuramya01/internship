class Student:

    def details(self, name, age=None, course=None):
        print("Name:", name)

        if age is not None:
            print("Age:", age)

        if course is not None:
            print("Course:", course)


obj = Student()

obj.details("Ramya")
print()

obj.details("Ramya", 17)
print()

obj.details("Ramya", 17, "CSE")