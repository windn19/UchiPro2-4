class RomanNumber:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'Число {self.number}'

    def __len__(self):
        return len(self.number)
    #
    # def __bool__(self):
    #     return bool(self.number)


number = RomanNumber(input())
print(number)
print(len(number))
print(bool(number))
