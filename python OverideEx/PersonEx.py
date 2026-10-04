class Person:
    def display(self):
        print("I am a person")


class Teacher(Person):
    def display(self):
        print("I am a teacher")


Teacher().display()