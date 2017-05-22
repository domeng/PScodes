# N,M은 중요하지 않다 [N*M,1]로 해석해도 똑같다
# 문양은 중요하지 않다 
# 전략 : 모르는 카드를 뒤집고 아는 카드가 나오면 100% 확률로 exit, 모르는 카드가 나오면 다시 모르는 카드 도전
# 아는 카드만 남으면 Solved
import sys
class PerfectMemory:
  def getExpectation(self,N,M):
    cache = {}
    def dp(known, unknown):
      if unknown <= 0:
        return known//2
      key = (known,unknown)
      if key in cache:
        return cache[key]
      exp = 0
      # case 1. pick a card in known symbols
      if known > 0:
        p = known/unknown
        exp += (1+dp(known-1,unknown-1)) * p
      if known < unknown:
        q = 1 - known/unknown
        # case 2. unknown -> unknown 
        exp += (1+dp(known+2,unknown-2)) * q * ((unknown-2-known)/(unknown-1))
        # case 3. unknown -> unknown (but lucky!)
        exp += (1+dp(known,unknown-2)) * q * (1/(unknown-1))
        # case 4. unknown -> known
        exp += (2+dp(known,unknown-2)) * q * (known/(unknown-1))
      cache[key] = exp
      return exp
    for total in range(0,N*M,2):
      for known in range(total//2,0,-1):
        unknown = total - known
        dp(known,unknown)
    return dp(0,N*M)

'''
print (PerfectMemory().getExpectation(1,2))
print (PerfectMemory().getExpectation(2,2))
print (PerfectMemory().getExpectation(2,3))
print (PerfectMemory().getExpectation(4,4))
print (PerfectMemory().getExpectation(50,47))
'''

