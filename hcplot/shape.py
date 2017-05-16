import math

class Shape(object):
    shapes = [ "circle", "triangle", "triangle-down", "diamond", "square" ]

    @classmethod
    def get(self, size):
        if size < len(Shape.shapes):
            return Shape.shapes[:size]
        else:
            factor = math.ceil(size / (len(Shape.shapes) - 3))
            return (Shape.shapes * factor)[:size]
