class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Точка с координатами {self.x}, {self.y}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'

class Point1(Point):
    pass


lst = [Point(3, 5), Point1(1, 2)]
print(lst[0])
print(lst)
# print(lst[1])