class Point:
    def __init__(self, *args):
        self.coords = args

    def __bool__(self):
        if 0 in self.coords:
            return False
        return True


my_point1 = Point(0, 2)
my_point2 = Point(3, -4, -5)
print(bool(my_point1))
if my_point2:
    print('Ни одна из координат точки не равна 0')