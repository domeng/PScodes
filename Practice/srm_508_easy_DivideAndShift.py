def divScore(x):
  r = 0
  for i in range(2,1001):
    while x%i == 0:
      r+=1
      x//=i
  if x>1:
    r+=1
  return r

class DivideAndShift:
  def getLeast(self, N, M):
    M-=1
    best=-1
    for i in range(1,1001):
      if N%i != 0:
        continue
      #sz = i and N/i
      p = i
      q = N // i
      pv = divScore(q)
      qv = divScore(p)
      ps = min(M%p,p-M%p) + pv
      qs = min(M%q,q-M%q) + qv
      ss = min(ps,qs)
      if ss < best or best < 0:
        best = ss
    return best

print(DivideAndShift().getLeast(56,14))
print(DivideAndShift().getLeast(49,5))
print(DivideAndShift().getLeast(256,7))
print(DivideAndShift().getLeast(6,1))
print(DivideAndShift().getLeast(77777,11111))

