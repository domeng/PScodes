class NetworkXOneTimePad:
  def crack(self,_p,_c):
    p = [int(x,2) for x in _p]
    c = [int(x,2) for x in _c]
    keys = set([x^c[0] for x in p])
    r = 0
    for key in keys:
      good = True
      for t in c:
        if not (t^key) in p:
          good = False
          break
      if good:
        r+=1
    print(r)
    return r





NetworkXOneTimePad().crack(["110","001"],["101","010"])
NetworkXOneTimePad().crack(["01","10"],["00"])