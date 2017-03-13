# https://community.topcoder.com/stat?c=problem_statement&pm=11357
'''
1;
pA-(T-rA)*dA
pB-(T-rA-rB)*dB
2;
pB-(T-rB)*dB
pA-(T-rA-rB)*dA
1-2;
(rA)*dB
(-rB)*dA
---------------
rA*dB-rB*dA < 0
rA/dA < rB/dB
.: therefore the solution seq's order will be same as the seq sorted by r_i/d_i
'''
import itertools
# To find out some pattern, it will solve smaller problem.
def solve(T, maxP, deltaP, reqT):
  #greedy
  def solveInternal(seq, show=False):
    nowT = 0
    nowP = 0
    for i in seq:
      nowT += reqT[i]
      p = maxP[i] - deltaP[i] * nowT
      if nowT > T or p < 0:
        break
      if show:
        print("%d : %d-%d(min)*%d=%d (req=%d d=%d mv=%.2f)" % (i,maxP[i],nowT,deltaP[i],p,reqT[i],deltaP[i],reqT[i]/deltaP[i]))
      nowP += p
    return nowP
  # In all possible n! seqs, calculate maxium profit by the greedy method
  n = len(maxP)
  seqs = [seq for seq in itertools.permutations(range(n))]
  vs = [solveInternal(s) for s in seqs]
  maxvs = max(vs)
  maxseq = seqs[vs.index(maxvs)]
  solveInternal(maxseq,True)
  return maxvs

'''
print(solve(74,[502],[2],[47]))
print(solve(40000,[100000, 100000],[1, 100000],[50000, 30000]))
print(solve(75,[250,500,1000],[2,4,8],[25, 25, 25]))
print(solve(30,[100, 100, 100000],[1, 1, 100],[15, 15, 30]))
'''

# The real solution
class TheProgrammingContestDivOne:
  def dp(self, T, _mP, _dP, _rT):
    table = [0] * (T+1)
    for mp,dp,rt in zip(_mP,_dP,_rT):
      for i in range(T,rt-1,-1):
        table[i] = max(table[i-rt] + mp - dp*i, table[i])
    return max(table)
  def find(self, T, maxPoints, pointsPerMinute, requiredTime):
    seq = range(len(maxPoints))
    seq = sorted(seq,key=lambda i:requiredTime[i]*1.0/pointsPerMinute[i])
    return self.dp(T,[maxPoints[i] for i in seq],[pointsPerMinute[i] for i in seq],[requiredTime[i] for i in seq])

for _ in range(5):
  import random
  n = 5
  T = 200
  A = [random.randint(1,10) * 10 for _ in range(n) ]
  B = [random.randint(1,10) for _ in range(n) ]
  C = [random.randint(1,10) for _ in range(n) ]
  print(solve(T,A,B,C))
  print(TheProgrammingContestDivOne().find(T,A,B,C))
