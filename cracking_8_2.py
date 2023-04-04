"""
"""

class Robot:
  def move(self, x, y, N, cur_path):
    if x > N or y > N:
      return
    if x >= N and y >= N:
      print('======Path=', cur_path)
      return
    self.move (x+1, y, N, cur_path + [(x+1, y)])
    self.move (x, y+1, N, cur_path + [(x, y+1)])
    
def run():
  R = Robot()
  R.move(0, 0, 5, [()])