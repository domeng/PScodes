# WW : do nothing
# BW : replace all black
# WB : replace all white
# BB : swap j,j+1

def transfer(a,b):
  n = len(a)
  dp = [[0,0] for _ in range(n)]
  dp[0] = [1,1]
  for i in range(1,n):
    for j in range(2): #0W 1B
      cmd = a[i-1] + a[i]
      for k in range(2):
        if cmd == 'WW':   jj,kk = j,k
        elif cmd == 'BW': jj,kk = 1,1
        elif cmd == 'WB': jj,kk = 0,0
        elif cmd == 'BB': jj,kk = k,j
        if 'WB'[jj] != b[i-1]:
          continue
        dp[i][kk] += dp[i-1][j]
        dp[i][kk] %= 1000000007
  return dp[-1][0] if b[-1] == 'W' else dp[-1][1]

class AlgridTwo:
  def makeProgram(self, mat):
    n = len(mat)
    cnt = 1
    for i in range(n-1):
      cnt *= transfer(mat[i],mat[i+1])
      cnt %= 1000000007
    return cnt

print(AlgridTwo().makeProgram(["BB", "WB"]))
print(AlgridTwo().makeProgram(["BBWBBB", "WBWBBW"]))
print(AlgridTwo().makeProgram(["BWBWBW", "WWWWWW", "WBBWBW"]))
print(AlgridTwo().makeProgram(["WWBWBWBWBWBWBWBW", "BWBWBWBWBWBWBWBB", "BWBWBWBWBWBWBWBW"]))
