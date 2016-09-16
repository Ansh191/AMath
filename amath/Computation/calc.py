

def slope(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    if dx == 0:
        return inf
    return Fraction(dy, dx)

