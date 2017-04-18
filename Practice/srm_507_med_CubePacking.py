#https://community.topcoder.com/stat?c=problem_statement&pm=11266
class CubePacking:
  def getMinimumVolume(self, Ns, Nb, L):
    V0 = Ns + Nb * (L**3)
    add = 0
    while True:
      V = V0 + add
      add += 1
      Cut = int(V**0.34) + 1
      for a in range(1,Cut):
        if V%a != 0:
          continue
        W = V/a
        Cut2 = int((V/a)**0.5)+1
        for b in range(a,Cut2):
          if W%b != 0:
            continue
          c = W/b
          aL,bL,cL = a//L,b//L,c//L
          if aL*bL*cL >= Nb:
            return V

print(CubePacking().getMinimumVolume(2,2,2))
print(CubePacking().getMinimumVolume(19,1,2))
print(CubePacking().getMinimumVolume(51,7,5))
print(CubePacking().getMinimumVolume(12345,987,10))
print(CubePacking().getMinimumVolume(1000**3,1000**2,10))
