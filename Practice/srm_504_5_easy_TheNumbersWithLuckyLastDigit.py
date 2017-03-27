class TheNumbersWithLuckyLastDigit:
  def find(self, n):
    best = -1
    for i in range(11):
      for j in range(11):
        if i == 0 and j == 0:
          continue
        num = i*4 + j*7
        if num > n or num%10 != n%10:
          continue
        if best < 0 or i+j < best:
          best = i+j
    return best

print(TheNumbersWithLuckyLastDigit().find(99))
print(TheNumbersWithLuckyLastDigit().find(11))
print(TheNumbersWithLuckyLastDigit().find(13))
print(TheNumbersWithLuckyLastDigit().find(1234567))

