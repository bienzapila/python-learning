class Shape:
    pass
class Circle(Shape):
    pass
class Square(Shape):
    pass

def get_shape_type(shape_object):
    if isinstance(shape_object, Circle):
        return 'Это круг'
    elif isinstance(shape_object, Square):
        return 'Это квадрат'
    else:
        if isinstance(shape_object, Shape):
            return 'Это общая фигура'