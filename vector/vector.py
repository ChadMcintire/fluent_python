import math

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    #__repr__()  returns a printable representation of the object, one of the ways
    #possible to create this object.  __repr__() is more useful for developers while __str__() is for end users.
    def __repr__(self):
    # the !r calls the __repr__ function
        return f'Vector({self.x!r}, {self.y!r})'

    #Return the Euclidean norm, sqrt(x*x + y*y). This is the length of the vector from the origin to point (x, y)
    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

print(Vector(1,2))
print(Vector(1,2) + Vector(1,3))
