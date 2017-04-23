def possible(a,b):
  if a.count('B') == 0:
    return b == ''
  if a.count('B') == b.count('A'):
    return b[0] == 'A'
  elif a.count('B') == b.count('A') + 1:
    return a[0] == 'B'
  return False

def possible_0(a,b):
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

def sim(prog):
  stk = ['','']
  z = 0
  for i in prog:
    stk[z] += i
    z = 0 if i == 'A' else 1
  return stk[0][::-1]+stk[1][::-1]

cnt = 0
sss = set()
dps = [[0]*19 for _ in range(5)]
def gens(A,B,C,tar,stk,sid,prog):
  if tar == '':
    global cnt,sss
    print (cnt,prog)
    meet = 0
    done = 0
    for i in range(len(prog)):
      if prog[i]=='C':
        dps[meet][done] += 1
        meet += 1
      else:
        done += 1
    cnt+=1
  if A>0:
    x = stk[sid]
    stk[sid] += 'A'
    gens(A-1,B,C,tar,stk,0,prog+'A')
    stk[sid] = x
  if B>0:
    x = stk[sid]
    stk[sid] += 'B'
    gens(A,B-1,C,tar,stk,1,prog+'B')
    stk[sid] = x
  if C>0:
    gen = stk[0][::-1] + stk[1][::-1]
    if tar.startswith(gen):
      gens(A,B,C-1,tar[len(gen):],['',''],0,prog+'C')

class Stackol:
  def countPrograms(self,fr, k):
    out = "".join(fr)
    #gens(out.count('A'),out.count('B'),k,out,['',''],0,'')
    out = "|" + out
    n = len(out)
    cnt = [0] * n
    cnt[0] = 1
    ret = 0
    x = []
    for _ in range(k):
      next = [0] * n 
      next[0] += cnt[0]
      for b in range(1,n):
        next[b] += cnt[b]
        for e in range(b,n):
          for j in range(b,e+1):
            A = out[b:j+1]
            B = out[j+1:e+1] if j<e else ''
            if possible_0(A,B):
              x.append(out[b:e+1])
              next[e] += cnt[b-1]
      ret += next[-1]
      print(next)
      cnt = next
    print(ret)
    return ret

'''
print(possible('B',''))
print(possible('B','A'))
print(possible('B','B'))
print(possible('AAAAABAAAAAA',''))
print(possible('BA','AB'))
'''
#Stackol().countPrograms(["ABAB"],3)
Stackol().countPrograms(["A"],2)
Stackol().countPrograms(["AAAA","BABA"],1)
Stackol().countPrograms(["AB"],2)
Stackol().countPrograms(["AAABABABAABA","AA","BBAB"],3)
Stackol().countPrograms(["AAAAAAAAAAAA","B"],4)
