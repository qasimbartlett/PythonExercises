"""
Sample implementation of quick sorted
Start with an iterator and a pivotIndex.
pull out the last element of the list.
Call it the pivot
Assume all elements to right of pivotIndex to be > than pivot

"""

class quicksort:
  def __init__(self, listofnum):
    self._listofnum = listofnum
    self.printList()
  
  def printList(self):
    print('List=',self._listofnum)

  def swapContents(self, i, j):
    temp = self._listofnum[i]
    self._listofnum[i] = self._listofnum[j]
    self._listofnum[j] = temp

  def sort(self, start, end):
    if start >= end:
      return
    
    pivot = self._listofnum[end]
    pivotIndex=start
    for i in range(start, end+1):
      if self._listofnum[i] < pivot:
        # Swap and increment pivotIndex
        self.swapContents(i,pivotIndex )
        pivotIndex += 1
    self._listofnum[i] = self._listofnum[pivotIndex]
    self._listofnum[pivotIndex] = pivot

    self.sort(start,pivotIndex-1)
    self.sort(pivotIndex+1, end)



def run():
  listofNumber = [2,1,6,4,8,5,7,3]
  #listofNumber = [2,1]
  qs = quicksort(listofNumber)
  qs.sort(0, len(listofNumber)-1)
  qs.printList()

  