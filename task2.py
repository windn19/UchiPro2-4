class Sequence:
    def __init__(self, *args):
        self.elements = list(args)

    def __str__(self):
        return f'Последовательность {self.elements}'

    def __len__(self):
        return len(self.elements)


elements = map(int, input().split())
seq = Sequence(*elements)
print(seq)
print(len(seq))
