class Point:
    def __init__(self, *args):
        self.coords = args

    def __abs__(self):
        return tuple(map(abs, self.coords))


my_point1 = Point(-1, 2)
my_point2 = Point(3, -4, -5)
print(abs(my_point1))
print(abs(my_point2))