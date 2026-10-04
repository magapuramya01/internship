class Display:

    def show(self, *args):
        for value in args:
            print(value)


obj = Display()

obj.show(10)
obj.show(10, 20)
obj.show(10, 20, 30)