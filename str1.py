class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Точка с координатами {self.x=} {self.y=}'


my_point = Point(3, 5)
print(my_point)
