def is_valid_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
        return False
    else:
        return True
