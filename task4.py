class PrimeNumbers:
    def __init__(self, n):
        self.n = n
        self.seq = list(self.prime())

    def prime(self):
        a = set(range(2, self.n ** 2))
        for i in range(2, self.n - 1):
            b = set(range(i * i, self.n ** 2, i))
            a -= b
        return list(a)[:self.n]

    def __str__(self):
        return f'Последовательность из {self.n} простых чисел {self.seq}'

    def total(self):
        return sum(self.seq)


num = int(input())
a = PrimeNumbers(num)
print(a)
print(a.total())
