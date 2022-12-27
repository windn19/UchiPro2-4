class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Точка с координатами {self.x}, {self.y}'

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


lst = [Point(3, 5), Point(1, 2)]
print(lst[0])
print(lst)
