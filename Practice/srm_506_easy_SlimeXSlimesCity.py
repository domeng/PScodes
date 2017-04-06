class SlimeXSlimesCity:
  def merge(self, pops):
    def honorable(pops,x):
      power = sum([z for z in pops if z <= x])
      enems = sorted([z for z in pops if z > x])
      for enem in enems:
        if power < enem:
          return 0
        power += enem
      return 1
    return sum([honorable(pops,x) for x in pops])

print(SlimeXSlimesCity().merge([2,3,4]))
print(SlimeXSlimesCity().merge([1,2,3]))
print(SlimeXSlimesCity().merge([8,2,3,8]))
print(SlimeXSlimesCity().merge([1000000000, 999999999, 999999998, 999999997]))
print(SlimeXSlimesCity().merge([1,1,1]))
print(SlimeXSlimesCity().merge([1, 2, 4, 6, 14, 16, 20]))