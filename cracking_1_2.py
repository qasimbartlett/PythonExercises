"""
cracking the google interview. 1.2
"""

class Sample:
  def ReverseString(self, in_string):
    for i in reversed(range(len(in_string))):
      char = in_string[i]
      print(char, end='')

def run():
  mytest = Sample()
  mytest.ReverseString('Idrees')  