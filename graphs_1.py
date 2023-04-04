class Graph:
  # best way to re graph is a a dict
  def __init__(self):
    self.vertices = dict()
  
  def addVertices(self, node, children):
    self.vertices[node] = children

  def BFS(self):
    nodes = [4]
    seen = []

    while nodes:
      node = nodes.pop(0)
      if node not in seen:
        print(node, end=' ')
        nodes += self.vertices[node]
        seen.append(node)
  
  def old_DFS(self, node, seen):   
    # DLR
    print(node, end=' ')
    for node in self.vertices[node]:
      if node not in seen:
        seen.append(node)
        self.old_DFS(node, seen)

  def FindAllPaths_DFS(self, node, target, pathSoFar):
    # print('1.node=', node, ' Path=', pathSoFar)
    if node == target:
      print('Target =', pathSoFar,  ' ', node)
      return
 
    for child in self.vertices[node]:
      if node not in pathSoFar:
        # pathSoFar.append(node)
        self.FindAllPaths_DFS(child, target,pathSoFar + [node])

  def xxxxDFS(self, node, pathSoFar):

    if not self.vertices[node]:
      print('---End seen; path=', pathSoFar + [node])
    if node in pathSoFar:
      print('---Loop seen; path=', pathSoFar + [node])

    for child in self.vertices[node]:
      if child not in pathSoFar:
        self.DFS(child, pathSoFar + [node])
      else:
        print('3.child already in path=', child, 'pathSofar=', pathSoFar + [node, child])

def run():
  my_graph = Graph()
  my_graph.addVertices(1, [1,3])
  my_graph.addVertices(2, [1])
  my_graph.addVertices(3, [2,5])
  my_graph.addVertices(4, [1,2,12,13])
  my_graph.addVertices(5, [6,8])
  my_graph.addVertices(6, [7,10,8])
  my_graph.addVertices(7, [10])
  my_graph.addVertices(8, [9,10])
  my_graph.addVertices(9, [5,11])
  my_graph.addVertices(10, [9,11,14,16])
  my_graph.addVertices(11, [12,14])
  my_graph.addVertices(12, [13])
  my_graph.addVertices(13, [11,15])
  my_graph.addVertices(14, [13])
  my_graph.addVertices(15, [14])
  my_graph.addVertices(16, [])
  print("--- BFS====")
  my_graph.BFS()
  print("\n\n--- DFS====")
  my_graph.old_DFS(4, [])
  # my_graph.DFS(4, [])
  print("\n\n--- FindAllPaths====")
  #my_graph.FindAllPaths_DFS(4, 14, [])
