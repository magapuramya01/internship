class Dog:
    def bark(self):
        print("Dog barks")


class RobotDog:
    def bark(self):
        print("Robot dog barks")


def make_bark(obj):
    obj.bark()


make_bark(Dog())
make_bark(RobotDog())