from itertools import product 

class RectangleArea:
  def minimumQueries(self, known):
    n = len(known)
    m = len(known[0])

    rs = list(range(n))
    cs = list(range(n,n+m))

    for i,j in product(range(n),range(m)):
      if known[i][j] == 'Y':
        a,b = rs[i],cs[j]
        for x in range(n):
          if rs[x] == a:
            rs[x] = b
        for x in range(m):
          if cs[x] == a:
            cs[x] = b
    return len(set(rs+cs))-1

print (RectangleArea().minimumQueries(["NN","NN"]))
print (RectangleArea().minimumQueries(["YNY", "NYN", "YNY"]))
print (RectangleArea().minimumQueries(["NNYYYNN", "NNNNNYN", "YYNNNNY", "NNNYNNN", "YYNNNNY"]))