import string
def col(ss):
  i = string.ascii_lowercase + string.ascii_uppercase
  st = sorted([(ss.count(x),x) for x in i],reverse=True)
  mapper = dict((st[i][1],i) for i in range(len(st)))
  return sum([mapper[i] for i in ss])

class RowsOrdering:
  def order(self, rows):
    c = len(rows[0])
    R = [col([r[i] for r in rows]) for i in range(c)]
    print(R)
    R = sorted(R,reverse=True)
    RT = [R[i]*(50**i) for i in range(len(R))]
    return (sum(RT) + len(rows)) %  1000000007

print( RowsOrdering().order(["bb", "cb", "ca"]) )
print( RowsOrdering().order(["abcd","ABCD"]) )
print( RowsOrdering().order(["Example","Problem"]) )
print( RowsOrdering().order(["a","a"]) )