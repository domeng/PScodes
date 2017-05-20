import bisect
class YetAnotherIncredibleMachine:
  def countWays(self, plPos, plLength, balls):
    balls = sorted(balls)
    ret = 1
    for x,l in zip(plPos, plLength):
      q = bisect.bisect_right(balls, x) - 1 # balls[q] <= x
      left = x - l
      if q >= 0:
        if balls[q] == x:
          return 0
        left = max(left,balls[q] + 1)
      right = x
      if q+1 < len(balls):
        right = min(right, balls[q+1] - l - 1)
      if right < left:
        return 0
      ret *= (right-left+1)
    return ret % 1000000009

print(YetAnotherIncredibleMachine().countWays([7],[10],[3,4]))
print(YetAnotherIncredibleMachine().countWays([1,4],[3,3],[2,7]))
print(YetAnotherIncredibleMachine().countWays([4,4,4],[10,9,8],[1,100]))
print(YetAnotherIncredibleMachine().countWays([0],[1],[0]))
print(YetAnotherIncredibleMachine().countWays([100, -4215, 251],[400, 10000, 2121],[5000, 2270, 8512, 6122]))