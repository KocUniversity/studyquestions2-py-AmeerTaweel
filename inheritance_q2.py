import math


class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        for i in range(self.n):
            self.sides[i] = float(input(f"Enter side {i}: "))

    def dispSides(self):
        for i in range(len(self.sides)):
            print(f"Side {i} is {self.sides[i]}")


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        """
        Uses Heron's formula for the area of a triangle
        """
        a, b, c = self.sides
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


t = Triangle()
t.inputSides()
t.dispSides()
print(f"The area of the triangle is {t.findArea()}")
