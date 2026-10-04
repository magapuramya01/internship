class Duck:
    def talk(self):
        print("Duck is talking")


class Person:
    def talk(self):
        print("Person is talking")


def make_talk(obj):
    obj.talk()


make_talk(Duck())
make_talk(Person())