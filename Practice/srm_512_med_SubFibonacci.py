class SubFibonacci:
  def maxElements(self, S):
    fibs = [1,1]
    while fibs[-1] <= 100000000:
      fibs.append(fibs[-1] + fibs[-2])
    #print(len(fibs)) = 40
    F = len(fibs)
    N = len(S)
    S = sorted(S)
    ToIndex = dict(zip(S,range(N)))
    UntilBest = [1] * N 
    FromBest = [1] * N
    for i in range(N):
      for j in range(i+1,N):
        for k in range(F):
          if S[i] * fibs[k] >= S[j]:
            break
          if (S[j] - S[i] * fibs[k]) % fibs[k+1] != 0:
            continue
          second_elment = (S[j] - S[i] * fibs[k]) // fibs[k+1]
          first_element = S[i]
          f_a, f_b = first_element, second_elment
          cnt = 1 
          while f_b <= 100000000:
            if f_b > first_element and f_b in ToIndex:
              cnt += 1
              UntilBest[ToIndex[f_b]] = max(UntilBest[ToIndex[f_b]], cnt)
            f_a,f_b = f_b,f_a+f_b
          FromBest[i] = max(FromBest[i], cnt)
    #print(S)
    #print (FromBest)
    #print (UntilBest)
    def maxC(li):
      if len(li) < 1:
        return 0
      return max(li)
    return max([maxC(UntilBest[:i]) + maxC(FromBest[i:]) for i in range(N)])

print (SubFibonacci().maxElements([1, 10946, 63245986, 63245990, 100000000]))
#print (SubFibonacci().maxElements([8,1,20,3,10]))
#print (SubFibonacci().maxElements([19, 47, 50, 58, 77, 99]))
#print (SubFibonacci().maxElements([512]))
#print (SubFibonacci().maxElements([3, 5, 7, 10, 13, 15, 20, 90]))
#print (SubFibonacci().maxElements([1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))
# first_element, some_element (nC2) = 50^2
# some_element decomposition = 40
# look_thorugh_after_elements = 50 
# => 830K