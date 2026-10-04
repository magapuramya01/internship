class Laptop:
    def power_on(self):
        print("Laptop is powered on")


class Desktop:
    def power_on(self):
        print("Desktop is powered on")


def turn_on(obj):
    obj.power_on()


turn_on(Laptop())
turn_on(Desktop())