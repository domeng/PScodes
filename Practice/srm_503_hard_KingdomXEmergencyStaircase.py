class KingdomXEmergencyStaircase:
  def determineCost(self, lb, rb, cost):
    lb = 'N' + lb
    rb = 'N' + rb
    n = max(len(lb), len(rb)) + len(cost) 
    lb += "N" * (n - len(lb))
    rb += "N" * (n - len(rb))
    self.W = len(cost)
    self.lb = lb
    self.rb = rb
    self.cost = cost
    self.lcount = [0] * n
    self.rcount = [0] * n
    self.n = n
    for i in range(1,n):
      self.lcount[i], self.rcount[i] = self.lcount[i-1],self.rcount[i-1]
      if lb[i] == 'Y': 
        self.lcount[i]+=1
      if rb[i] == 'Y':
        self.rcount[i]+=1
    self.visit = {}
    self.cache = {}
    return self.solveFunction(('E',0,0,0,0))

  def pieceGenerator(self, tp, p1, p2, p3, p4):
    def dist(a,b,d):
      if (b-a) * d < 0: 
        i = (self.W//2 - max(a,b) + min(a,b)) - 1
      else:
        i = (self.W//2 + max(a,b) - min(a,b)) - 1
      try:
        return self.cost[i]
      except:
        return -1
    def same(a,b):
      try:
        return self.cost[max(a,b) - min(a,b) - 1]
      except:
        return -1
    h = '!' if tp[0] == '!' else ''
    if 'A' in tp:
      for k in range(p1, p2 + 1): #[p1,p2]
        if k != p2:
          yield [dist(k,p3,1),(h+'A',p1,k,p3,p4),(h+'B',k,p2,p3,0)]
        if k != p1:
          yield [dist(k,p4,-1),(h+'D',p1,k,p4,0),(h+'A',k,p2,p3,p4)]
    elif 'B' in tp:
      for k in range(p1+1, p2): #(p1,p2)
        yield [dist(k,p3,1),(h+'B',p1,k,p3,0),(h+'B',k,p2,p3,0)]
        yield [same(p1,k),(h+'C',p1,k,0,0),(h+'A',k,p2,p3,p1+self.W)]
    elif 'C' in tp:
      for k in range(p1+1,p2): #(p1,p2)
        yield [same(k,p2),(h+'B',p1,k,p2-self.W,0),(h+'C',k,p2,0,0)]
        yield [dist(k,p3,-1),(h+'C',p1,k,0,0),(h+'D',k,p2,p1+self.W,0)]
    elif 'D' in tp:
      for k in range(p1+1, p2): #(p1,p2)
        yield [dist(k,p3,-1),(h+'D',p1,k,p3,0),(h+'D',k,p2,p3,0)]
        yield [same(k,p2),(h+'A',p1,k,p2-self.W,p3),(h+'C',k,p2,0,0)]
    elif 'E' in tp:
      for k in range(p1+1,self.n):
        yield [dist(k,p2,-1),('D',p1,k,p2,0),('E',k,p2,0,0)]
      for k in range(p2+1,self.n):
        yield [dist(k,p1,-1),('E',p1,k,0,0),('!D',p2,k,p1,0)]

  def checkEmpty(self, tp, p1, p2, p3, p4):
    if '!' in tp: # !A !B !C !D
      return (self.rcount[p2-1] - self.rcount[p1]) == 0
    elif tp != 'E': # A B C D
      return (self.lcount[p2-1] - self.lcount[p1]) == 0
    else: # E
      return (self.lcount[-1] == self.lcount[p1] and self.rcount[-1] == self.rcount[p2])

  def solveFunction(self, state):
    if self.visit.get(state,0) == 1:
      return self.cache[state]
    self.visit[state] = 1
    if self.checkEmpty(*state):
      self.cache[state] = 0
      return 0
    best = -1
    for D,A,B in self.pieceGenerator(*state):
      if D < 0:
        continue
      rx = self.solveFunction(A) + self.solveFunction(B) + D
      if best < 0 or rx < best:
        best = rx
    self.cache[state] = best
    return best

print(KingdomXEmergencyStaircase().determineCost("YNYY","NNNY",[10,40,18,25]))
'''
print(KingdomXEmergencyStaircase().determineCost("N","Y",[1,1000]))
print(KingdomXEmergencyStaircase().determineCost("NNNNNNNY","NNNNNNNY",[1, 2]))
print(KingdomXEmergencyStaircase().determineCost("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN","NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNY",
  [800000000,800000000,800000000,800000000,800000000,800000000,800000000,800000000]))
print(KingdomXEmergencyStaircase().determineCost("NNY","NNYYY",[10000, 10, 40, 10000, 80, 80]))
'''
'''
{"YYNYNNNYNNNYYY", "NYYYNNYNNYYNYYYYNYYYNNYYYYYY", {734359722, 811163980, 507608624, 507992981}}
Expected:
17046879788
Received:
16593761949
'''