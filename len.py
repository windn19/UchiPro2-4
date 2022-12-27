class Point:
    def __init__(self, *args):
        self.coords = args

    def __len__(self):
        return len(self.coords)


my_point1 = Point(1, 2)
my_point2 = Point(3, 4, 5)
print(len(my_point1))
print(len(my_point2))
