class PrimeNumbers:
   def __init__(self, n):
       number = 2
       numbers = []
       while len(numbers) < n:
           for d in range(2, number - 1):
               if number % d == 0:
                   break
           else:
               numbers.append(number)
           number += 1
       self.numbers = numbers

   def __str__(self):
       return f'Последовательность из {len(self.numbers)} простых чисел {self.numbers}'

   def total(self):
       return sum(self.numbers)


n = int(input())
numbers = PrimeNumbers(n)
print(numbers)
print(numbers.total())