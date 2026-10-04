class Bird:
    def fly(self):
        print("Bird can fly")


class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")


class Eagle(Bird):
    def fly(self):
        print("Eagle can fly")


class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")


Sparrow().fly()
Eagle().fly()
Penguin().fly()