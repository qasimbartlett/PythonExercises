"""
"""

class Subset: 
  def subsets(self, items):
    if len(items) == 0:
      return items
  
    print('\n\nitems=', items)
    x = items.pop()
    print('items=', items, ' x=',x)
    s2 = self.subsets(items)
    print('s2=', s2)
    s1 = [x] + s2 
    print('s1=', s1)
    s3 = [] + s2 
    print('s3=', s3)



def run():
  S = Subset()
  S.subsets([1,2,3])

