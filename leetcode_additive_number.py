"""
https://leetcode.com/problems/additive-number/

"""
import re

class addNum():
  def __init__(self, num_str):
    self.num_str = num_str
    print('Idrees num=', self.num_str)

    pos1 = 0
    win1 = 1
    while pos1+win1 < len(num_str):
      num1 = int(num_str[pos1:pos1+win1])
      print('Num1=%d', num1)
      pos2 = pos1+1
      win2 = 1
      while pos2 + win2 < len(num_str):
        num2 = int(num_str[pos2:pos2+win2])
        print('Num2=', num2)
        num3 = num1 + num2
        print('Looking for Num3=%d', num3)
        matched = re.match(str(num3),num_str[pos2+win2:])
        if matched:
          print('num1=%d num2=%d num3=%d found', num1, num2, num3)
        else:
          win2 += 1
      win1 += 10


def run():
  a = addNum('199100199')
