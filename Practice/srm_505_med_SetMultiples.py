class SetMultiples:
  def smallestSubset(self,a,b,c,d):
    c = max(c,d//2+1)
    a = max(a,b//2+1)

    ans = (d-c+1) + (b-a+1)
    while a<=b:
      k = (c+b-1)//b
      l,r = (c+k-1)//k,d//k
      ans -= max(0,min(r,b)-max(a,l) + 1)
      b = l-1
    return ans

#SetMultiples().smallestSubset(1,1,2,2)
#SetMultiples().smallestSubset(1,2,3,4)
#SetMultiples().smallestSubset(2,3,5,7)
#SetMultiples().smallestSubset(1,10,100,1000)
print(SetMultiples().smallestSubset(1000000000,2000000000,9000000000,10000000000))
