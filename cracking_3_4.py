"""
Tower of hanoi
Assume 
Tower1 = T1 = [1,2,3,4,5,6]
We need to move the #s or rings to T2 in order
T2 = [1,2,3,4,5,6]
"""

class TowerOfHanoi:
  def solve(self):
    T1 = [1, 2, 3, 4, 5, 6]
    T2 = []
    T3 = []
    print('Idrees T1=', T1.reverse())
    for i in range(len(T1)):
      T2.append(T1.pop())
    print('Idrees T2=', T2)
    for i in range(len(T2)):
      T3.append(T2.pop())
    print('Idrees T3=', T3)

def run():
  T = TowerOfHanoi()
  T.solve()

