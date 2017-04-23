def possible(a,b):
  if len(a)<1:
    return False
  c = [len(a)-1,len(b)-1]
  i = 0
  while c[0] >=0 or c[1]>=0:
    if i == 0:
      if c[0] < 0:
        return False
      z = a[c[0]]
      c[0]-=1
    else:
      if c[1] < 0:
        return False
      z = b[c[1]]
      c[1]-=1
    i = 0 if z=='A' else 1
  return True

class Stackol:
  def countPrograms(self,fr, k):
    out = "|" + "".join(fr)
    n = len(out)
    cnt = [0] * n
    cnt[0] = 1
    ret = 0
    for _ in range(k):
      next = [0] * n 
      next[0] = 1
      for b in range(1,n):
        next[b] += cnt[b]
        for e in range(b,n):
          for j in range(b,e+1):
            if possible(out[b:j+1],out[j+1:e+1]):
              next[e] += cnt[b-1]
              break
      ret += next[-1]
      cnt = next
    print(ret)
    return ret

Stackol().countPrograms(["A"],2)
Stackol().countPrograms(["AAAA","BABA"],1)
Stackol().countPrograms(["AB"],2)
Stackol().countPrograms(["AAABABABAABA","AA","BBAB"],3)
Stackol().countPrograms(["AAAAAAAAAAAA","B"],4)
