#https://community.topcoder.com/stat?c=problem_statement&pm=11266
class CubePacking:
  def getMinimumVolume(self, Ns, Nb, L):
    cut = int(Nb**0.34)+1
    z = 0
    for a in range(1,cut):
      for b in range(a,Nb):
        A = a*b
        if (Nb+A-1)//A < b:
          break
        c = (Nb+A-1)//A
        z += 1
        u = max(0, Ns-(a*b*c-Nb)*(L**3))
        dims = [a*L,b*L,c*L]
    print(z)
CubePacking().getMinimumVolume(12345,1000*1000,10)
