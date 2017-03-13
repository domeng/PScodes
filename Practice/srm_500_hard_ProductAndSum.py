# https://community.topcoder.com/stat?c=problem_statement&pm=11345
# in real, it would be failed (TLE, 3.6s for the worst case)
def measure(func):
  import datetime
  def measure_call(*args, **kwargs):
    begin = datetime.datetime.now()
    func(*args, **kwargs)
    print("Elapsed = %f secs" % ((datetime.datetime.now() - begin).total_seconds()))
  return measure_call

@measure
def solve(l2,l3,l5,l7,S):
  M = 500500573
  f = [1]
  ones = [0]
  for i in range(1,2501):
    f.append( (f[-1] * i) % M )
    ones.append((ones[-1] * 10 + 1) % M)
  def pow(x,p,mod):
    if p==0:
      return 1
    t = pow(x,p//2,mod) ** 2
    if p%2==1:
      t*=x
    return t%mod
  inv_f = [ pow(x, M-2, M) for x in f ]
  z = 0
  c = [0]*10
  l = [100]*10
  l[2],l[3],l[5],l[7] = l2,l3,l5,l7
  c[5],c[7] = l5,l7
  subs = [0] * 5
  subf = [0] * 5
  subs[0] = c[5] * 5 + c[7] * 7
  subf[0] = (inv_f[c[5]] * inv_f[c[7]]) % M
  def update(idx, val):
    subs[idx] = subs[idx-1] + c[val] * val
    subf[idx] = (subf[idx-1] * inv_f[c[val]]) % M
    return subs[idx] > S
  for c[6] in range(min(l[2],l[3])+1):
    if update(1,6): break
    for c[4] in range((l[2]-c[6])//2+1):
      if update(2,4): break
      for c[8] in range((l[2]-c[4]*2-c[6])//3+1):
        if update(3,8): break
        for c[9] in range((l[3]-c[6])//2+1):
          c[2] = l[2] - (c[4]*2+c[8]*3+c[6])
          c[3] = l[3] - (c[9]*2+c[6])
          if c[2] < 0 or c[3] < 0:
            break

          subs[4] = subs[3] + c[9] * 9 + c[2] * 2 + c[3] * 3
          c[1] = S - subs[4]
          if c[1] < 0:
            break

          subf[4] = (subf[3] * inv_f[c[9]]) % M
          subf[4] *= (inv_f[c[2]] * inv_f[c[3]] * inv_f[c[1]]) % M
          subf[4] %= M

          digits = sum(c)
          xsum = S * subf[4] * f[digits-1] * ones[digits]
          xsum %= M
          z += xsum
          z %= M
  print (z%M)
'''
solve(2,0,0,0,4)
solve(0,0,0,0,10)
solve(2,0,0,0,5)
solve(1,1,1,1,10)
solve(5,5,5,5,100)
'''
solve(100,100,100,100,2500) #170475026
