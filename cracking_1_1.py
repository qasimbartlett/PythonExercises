"""
cracking the google interview. 1.1
"""
from collections import defaultdict

class Sample:
  def UniqChar(self, in_string):
    # char_count = dict()
    char_count = defaultdict(int)
    for i in range(len(in_string)):
      char = in_string[i]
      char_count[char] += 1 
    for (key, val) in char_count.items():
      if val > 1:
        print('This char=', key, ' occurs ', val, 'times')
        return


def run():
  mytest = Sample()
  mytest.UniqChar('abbajabbadabba')  