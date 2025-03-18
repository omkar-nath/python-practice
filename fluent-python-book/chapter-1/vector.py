from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r,%r)" % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":
    vector1 = Vector(1, 2)
    vector2 = Vector(2, 3)
    print("Addition of two vectors:", vector1 + vector2)
    print("Value of a vector:", abs(Vector(3, 4)))
    print("Multiplication", Vector(3, 5) * 5)
