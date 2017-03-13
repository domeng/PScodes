# https://community.topcoder.com/stat?c=problem_statement&pm=11063
# assume that there are some villages ABCDE for a village i where dist(a,i) < dist(b,i) < dist(c,i) < ...
# village A can be connected to the system before i do with 1/2 probability.
# village A is not connected, and B is connected to the system before i with 1/6 probability (<= only b~i~a works in all possible 6 combinations)
# village AB is not connected, and C is connected with 1/12 probability.
# you can find out that the sequence will be (n-1)!/(n+1)! = 1/n(n+1) 
# meanwhile if you meet a city, then you don't need care about villages more. 

import itertools
class KingdomXCitiesandVillages:
  def determineLength(self, cx, cy, vx, vy):
    n = len(cx)
    m = len(vx)
    allc = [(cx[i],cy[i],'c') for i in range(n)]
    allv = [(vx[i],vy[i],'v') for i in range(m)]
    alls = itertools.chain(allc,allv)
    ret = 0
    for x,y,_ in allv:
      def dist(m):
        return ((m[0]-x)**2+(m[1]-y)**2)**0.5
      alls = sorted(alls, key=lambda m:(dist(m),m[2]))
      count = 0
      prob = 1
      for mx,my,mt in alls:
        count += 1
        if count == 1:
          continue
        if mt == 'c':
          ret += dist((mx,my)) * prob
          break
        p = 1.0/count/(count-1)
        ret += dist((mx,my)) * p
        prob -= p
    return ret