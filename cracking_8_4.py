"""
given a string find all permutations

"""

class cracking_8_4:

  def permutations2(self, in_str):
    if len(in_str) <= 1:
      return in_str

    perms = []
    for c in in_str:
      sub_str = in_str.replace(c, '')
      for sub_perm in self.permutations(sub_str):
        perms.append(c + sub_perm)
    print('perms=                   ', perms)
    return perms

  # remove character from ith position
  def pop_out(self, i, in_str):
    return in_str[0:i] + in_str[i+1:]

  def permutations(self, in_str):
    if len(in_str) <= 1:
      return in_str

    perms = []
    for i in range(len(in_str)):
      first_char = in_str[i]
      remaining_str = self.pop_out(i, in_str)
      for sub_perm in self.permutations(remaining_str):
        perms.append(first_char + sub_perm)
    print('permutations=', perms)
    return perms





def run():
  in_str = 'abc'
  p = cracking_8_4()
  p.permutations(in_str)