# http://tinyurl.com/y9c2fjhn
class Node:
  def __init__(self, data):
    self.data=data
    self.alreadyVisited = False
    self.children = []
    # print('Node created; data=', data)

  def printNode(self):
    print(self.data, end=' ')

  def returnData(self):
    return self.data

  def addChildren(self, children):
    # print('before Children added size', len(self.children))
    self.children += children
    # print('After Children added size', len(self.children))
    # self.printChildren()
    # print("---------   print children done ----\n\n\n")

  def returnChildren(self):
    return self.children
  
  def printChildren(self):
    for child in self.children:
      # print("=== printing child=====", end=' ')
      child.printNode()
    # print("\n\n")
    
  def MarkVisited(self):
    self.alreadyVisited = True
  
  def IsalreadyVisited(self):
    return self.alreadyVisited

class Graph:
  def __init__(self):
    self.n1 = Node(1)
    self.n2 = Node(2)
    self.n3 = Node(3)
    self.n4 = Node(4)
    self.n5 = Node(5)
    self.n6 = Node(6)
    self.n7 = Node(7)
    self.n8 = Node(8)
    self.n9 = Node(9)
    self.n10 = Node(10)
    self.n11 = Node(11)
    self.n12 = Node(12)
    self.n13 = Node(13)
    self.n14 = Node(14)
    self.n15 = Node(15)

    self.n1.addChildren([self.n1,self.n3])
    self.n2.addChildren([self.n1])
    self.n3.addChildren([self.n2, self.n5])
    self.n4.addChildren([self.n1, self.n2,self.n12,self.n13])
    self.n5.addChildren([self.n6,self.n8])
    self.n6.addChildren([self.n8,self.n10,self.n7])
    self.n7.addChildren([self.n10])
    self.n8.addChildren([self.n9,self.n10])
    self.n9.addChildren([self.n5,self.n11])
    self.n10.addChildren([self.n14,self.n11,self.n9])
    self.n11.addChildren([self.n14,self.n12])
    self.n12.addChildren([self.n13])
    self.n13.addChildren([self.n11,self.n15])
    self.n14.addChildren([self.n13])
    self.n15.addChildren([self.n14])

    self.path = []

  def BreathFirstSearch_pathsToNode(self, currentNode, targetNode, pathSoFar):
    
    if currentNode.returnData() == targetNode.returnData():
      print("idrees-target-found: Path=",pathSoFar,"->",currentNode.returnData())
      return 
    if not currentNode.children:
      print("idrees-dead-end          =",pathSoFar,"->",currentNode.returnData())
      return
    if currentNode.returnData() in pathSoFar:
      print ("idrees-loop-detected     =",pathSoFar,"->",currentNode.returnData())
      return

    for node in currentNode.returnChildren():
      self.BreathFirstSearch_pathsToNode(node,targetNode,pathSoFar + [currentNode.returnData()])
      
  def BFS(self):
    all_nodes = [self.n4]
    seen = [self.n4.returnData()]
    print('seen=', seen)

    while (all_nodes):
      node = all_nodes.pop(0)
      print(node.returnData, end = ' ')
      for child in node.children:
        if child.returnData() not in seen:
          all_nodes.append(child)
          seen.append(child.returnData())
          print('seen=', seen)

  def FindPaths(self):
    self.BreathFirstSearch_pathsToNode(self.n4, self.n15, [])

def run():
  mygraph = Graph()
  # mygraph.FindPaths()
  mygraph.BFS()
  # mygraph.Walk()
  print('Idrees ')


