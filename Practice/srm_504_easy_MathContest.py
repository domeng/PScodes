class MathContest:
  def countBlack(self, ballSequence, repetitions):
    seq = ballSequence * repetitions
    cs = [0,len(seq)-1]
    s = 0
    iv = 0
    cnt = ['B','W']
    dir = [1,-1]
    ret = 0
    while cs[0]<=cs[1]:
      now = seq[cs[s]]
      cs[s] += dir[s]
      if now == cnt[iv]: #black
        ret += 1
        iv ^= 1
      else: #white
        s ^= 1
    return ret