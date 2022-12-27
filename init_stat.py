class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y


my_point = Point(3, 5)
print(my_point.get_coordinates())
