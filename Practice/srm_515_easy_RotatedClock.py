def solve(h_,m_):
  mm = (h_%30)*2
  m__ = mm * 6
  if m_%30 != m__%30:
    return ''
  h__ = h_ + (m__ - m_)
  if h__ < 0: h__ += 360
  if h__ >= 360: h__ -= 360
  hh = h__//30
  ret = '{:02d}:{:02d}'.format(hh,mm)
  print(h_,m_,ret)
  return ret

class RotatedClock:
  def getEarliest(self,h_,m_):
    return solve(h_,m_)
