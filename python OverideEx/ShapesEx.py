class Shape:
    def area(self):
        print("Area of shape")


class Rectangle(Shape):
    def area(self):
        print("Area of rectangle")


class Circle(Shape):
    def area(self):
        print("Area of circle")


class Triangle(Shape):
    def area(self):
        print("Area of triangle")


Rectangle().area()
Circle().area()
Triangle().area()