def add_complex(z1, z2):
    return ComplexRI(z1.real + z2.real, z1.imag + z2.imag)

def mul_complex(z1, z2):
    return ComplexMA(z1.magnitude * z2.magnitude, z1.angle + z2.angle)

from math import atan2

class ComplexRI(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        ComplexRI.__add__ = lambda self, other: add_complex(self, other)
        ComplexRI.__mul__ = lambda self, other: mul_complex(self, other)
        ComplexRI.__bool__ = lambda self: self.real != 0 or self.imag != 0

    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    @property
    def angle(self):
        return atan2(self.imag, self.real)
    def __repr__(self):
        return 'ComplexRI({0}, {1})'.format(self.real, self.imag)
    
from math import sin, cos
class ComplexMA(object):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
        ComplexMA.__add__ = lambda self, other: add_complex(self, other)
        ComplexMA.__mul__ = lambda self, other: mul_complex(self, other)
        ComplexMA.__bool__ = lambda self: self.magnitude != 0

    @property
    def real(self):
        return self.magnitude * cos(self.angle)
    @property
    def imag(self):
        return self.magnitude * sin(self.angle)
    def __repr__(self):
        return 'ComplexMA({0}, {1})'.format(self.magnitude, self.angle)
    
if __name__ == "__main__":
    from math import pi
    print(ComplexRI(1, 2) + ComplexMA(2, pi/2))
    print(ComplexRI(0, 1) * ComplexRI(0, 1))
    print(bool(ComplexRI(1, 2)))
    print(bool(ComplexRI(0, 0)))
