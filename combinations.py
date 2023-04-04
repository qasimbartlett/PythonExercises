"""
combination of n things taken r at a time
nCr = n-1Cr + n-1Cr-1
"""
class combinations:

  def combos(self, n, r):
    if n == r:
      return 1
    if n == 1:
      return 1
    if r == 1:
      return n
     
    return self.combos (n-1, r) + self.combos(n-1, r-1)

def run():
  n = 3
  r = 2
  c = combinations()
  x = c.combos(n, r)
  print('Combos=', x)