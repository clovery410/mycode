class Square(object):
    def __init__(self, side):
        self.side = side

class Rect(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

def type_tag(s):
    return type_tag.tags[type(s)]

type_tag.tags = {Square: 's', Rect: 'r'}

def apply(operator_name, shape):
    """Apply operator to shape.

    >>> apply('area', Square(10))
    100
    >>> apply('perimeter', Square(5))
    20
    >>> apply('area', Rect(5, 10))
    50
    >>> apply('perimeter', Rect(2, 4))
    12
    """
    types = (operator_name, type_tag(shape))
    return apply.implementations[types](shape)

apply.implementations = {}
apply.implementations[('area', 's')] = lambda x: x.side ** 2
apply.implementations[('perimeter', 's')] = lambda x: x.side * 4
apply.implementations[('area', 'r')] = lambda x: x.width * x.height
apply.implementations[('perimeter', 'r')] = lambda x: (x.width + x.height) * 2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
