class Lion:
    def sound(self):
        print("Lion roars")


class Dog:
    def sound(self):
        print("Dog barks")


class Baby:
    def sound(self):
        print("Baby cries")


def make_sound(obj):
    obj.sound()


make_sound(Lion())
make_sound(Dog())
make_sound(Baby())