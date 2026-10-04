class Area:

    def calculate(self, a, b=None):
        if b is None:
            # square
            return a * a
        else:
            # rectangle
            return a * b


obj = Area()

print("Square:", obj.calculate(5))
print("Rectangle:", obj.calculate(5, 10))