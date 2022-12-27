class Point:
    def __str__(self):
        print('Был вызван метод __str__')
        return 'Точка'


my_point = Point()
str(my_point)
print(my_point)