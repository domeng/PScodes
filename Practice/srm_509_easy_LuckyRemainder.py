class LuckyRemainder:
  def getLuckyRemainder(self,ss):
    n = len(ss)
    mul = (2**(n-1)) % 9
    return sum([(ord(e)-ord('0'))*mul for e in ss]) % 9

