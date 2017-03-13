# https://community.topcoder.com/stat?c=problem_statement&pm=11204
# WBWBWBWBWB
# WB B B B
#   W W W WB
# you can easily find out that answer <= 2 

class ToastXToast:
  def bake(self, under, over):
    if min(over) < min(under) or max(over) < max(under): # start with B or end with W
      return -1
    # WB
    if max(under) < min(over):
      return 1
    # WB(WB)+
    return 2