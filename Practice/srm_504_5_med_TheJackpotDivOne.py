class TheJackpotDivOne:
  def find(self, data, money):
    data = sorted(data)
    n = len(data)
    while money > 0:
      if data[0] == data[-1]: #if len(set(data)) == 1:
        break
      tar_avg = (sum(data)+n)//n
      agift = min(tar_avg-data[0],money)
      data[0] += agift
      money -= agift
      data = sorted(data)
    if money > 0:
      base_gift = money//n
      mod_gift = money%n
      for i in range(n):
        if i < mod_gift:
          data[i] += 1
        data[i] += base_gift
    return sorted(data)

print(TheJackpotDivOne().find([1, 2, 3, 4],2))
print(TheJackpotDivOne().find([4],7))
print(TheJackpotDivOne().find([4, 44, 7, 77],47))
print(TheJackpotDivOne().find([4, 10, 8, 3, 6, 5, 8, 3, 7, 5],10**18))
