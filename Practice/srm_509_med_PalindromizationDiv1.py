import string
class PalindromizationDiv1:
  #int getMinimumCost(String word, String[] operations)
  def getMinimumCost(self, word, ops_):
    tb = string.ascii_lowercase + ' ' #None
    Z = len(tb)
    ops = [x.split() for x in ops_]
    c_trans = [ [987654321]*Z for _ in range(Z) ]
    for o in ops:
      if o[0] == 'erase':
        c_trans[tb.index(o[1])][Z-1] = int(o[2])
      if o[0] == 'add':
        c_trans[Z-1][tb.index(o[1])] = int(o[2])
      if o[0] == 'change':
        c_trans[tb.index(o[1])][tb.index(o[2])] = int(o[3])
    for i in range(Z):
      c_trans[i][i] = 0
    for k in range(Z):
      for i in range(Z):
        for j in range(Z):
          if c_trans[i][k] + c_trans[k][j] < c_trans[i][j]:
            c_trans[i][j] = c_trans[i][k] + c_trans[k][j]
    n = len(word)
    table = [[0]*n for _ in range(n+1)]
    froms = {}
    for D in range(n):
      for L in range(n-D):
        R = L+D
        best = 987654321
        L_a = tb.index(word[L])
        L_b = tb.index(word[R])
        for k in range(Z):
          best = min(best, table[L+1][R-1] + c_trans[L_a][k] + c_trans[L_b][k]) #a->k<-b
          best = min(best, table[L+1][R] + c_trans[L_a][k] + c_trans[Z-1][k]) #a->k,None->k
          best = min(best, table[L][R-1] + c_trans[Z-1][k] + c_trans[L_b][k]) #None->k,b->k
        best = min(best, table[L+1][R] + c_trans[L_a][Z-1]) #erase a
        best = min(best, table[L][R-1] + c_trans[L_b][Z-1]) #erase b
        best = min(best, table[L+1][R] + c_trans[Z-1][L_a]) #add a to right
        best = min(best, table[L][R-1] + c_trans[Z-1][L_b]) #add b to left
        table[L][R] = best
    return table[0][n-1] if table[0][n-1] < 987654321 else -1




print(PalindromizationDiv1().getMinimumCost("hidxennvjqbfuaukugdfqddzstmlkkowfzqyfsfjq", ["change o j 51208", "change g f 32365", "change r h 57857", "change t b 82814", "add n 55311", "change t q 44336", "erase s 3638", "change p q 52249", "change u o 85395", "change p t 39867", "change q w 8672", "add d 79495", "change s t 46535", "erase m 18827", "change r n 45267", "add s 84863", "change w l 89256", "change a f 49049", "change y f 3283", "add c 61103", "change m i 4846", "erase b 18280", "erase c 32074", "change h z 62221", "change g h 61625", "change o i 44005", "change o k 80694", "change e l 39484", "erase j 92058", "change u d 30783", "add r 74995", "change g a 44914", "change z m 28587", "erase r 3258", "erase k 91503", "erase u 32899", "change f k 41193", "change i r 94746", "change y d 42267", "change g v 49092", "add v 93460", "add j 40452", "change b e 4702"]

))

