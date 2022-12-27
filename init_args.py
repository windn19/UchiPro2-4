class Point:
    def __init__(self, *args):
        # self.coords = args
        for i in range(len(args)):
            setattr(self, f'a{i}', args[i])

    def get_coordinates(self):
        return self.coords


my_point1 = Point(3)
my_point2 = Point(3, 5)
my_point3 = Point(3, 5, 7)
# print(my_point1.get_coordinates())
# print(my_point2.get_coordinates())
# print(my_point3.get_coordinates())