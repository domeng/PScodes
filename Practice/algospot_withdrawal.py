T = int(input())
for _ in range(T):
  n,k = map(int,input().split())
  dt = map(int,input().split())
  dt = list(zip(dt,dt))
  lo,hi = 0.0,1.0
  for i in range(64):
    mid = (lo+hi)/2
    def v(x): return x[0]-x[1]*mid
    if sum(sorted(map(v,dt))[:k]) <= 0:
      hi = mid
    else:
      lo = mid
  print(mid)