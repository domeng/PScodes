# let's watch how it spreads first
import random

def spread(N,M):
  test_cnt = 500000
  result = {}
  for i in range(test_cnt):
    n,m = N,M
    while True:
      dice = random.randint(1,6)
      if dice == 4:
        result[(n,m)] = result.get((n,m),0)+1
        break
      elif dice % 2 == 0:
        n -= 1
        m -= 1
        result[(n,m)] = result.get((n,m),0)+1
        break
      else:
        m -= 1
        if m<0:
          m=n-1
  print ('-'*10,(N,M),'-'*10)
  for k,v in sorted(result.items()):
    print (k,v/test_cnt*100)

spread(5,0)
spread(5,1)
spread(5,2)
spread(5,3)
spread(5,4)

