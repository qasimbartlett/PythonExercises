class Node:
    def __init__(self, key, left=None, right=None):
        self.data = key
        self.left = left
        self.right = right

    def printNode(self):
        return self.data


class Tree:
    def __init__(self):
        # Trees#1: http://tinyurl.com/y9c2fjhn
        """
    self.n1 = Node(1)
    self.n3 = Node(3)
    self.n5 = Node(5)
    self.n7 = Node(7)
    self.n9 = Node(9)
    self.n11 = Node(11)
    self.n13 = Node(13)
    self.n15 = Node(15)
    self.n2  = Node(2,  self.n1, self.n3)
    self.n6  = Node(6,  self.n5, self.n7)
    self.n10 = Node(10, self.n9, self.n11)
    self.n14 = Node(14, self.n13, self.n15)
    self.n4  = Node(4 , self.n2, self.n6)
    self.n12 = Node(12, self.n10, self.n14)
    self.root  = Node(8 , self.n4, self.n12)
	  """
        # Tree #2: http://tinyurl.com/y9c2fjhn
        self.n1 = Node(1)
        self.n3 = Node(3)
        self.n6 = Node(6)
        self.n9 = Node(9)
        self.n11 = Node(11)
        self.n15 = Node(15)
        self.n2 = Node(2, self.n1, self.n3)
        self.n4 = Node(4, self.n2, self.n6)
        self.n10 = Node(10, self.n9, self.n11)
        self.n14 = Node(14, self.n10, self.n15)
        self.n12 = Node(12, right=self.n14)
        self.root = Node(8, self.n4, self.n12)

    def GiveRootNode(self):
        return self.root

    def LDR(self, node):
        if node == None:
            return
        self.LDR(node.left)
        print(node.printNode(), end=' ')
        self.LDR(node.right)

    def DLR(self, node):
        if node == None:
            return
        print(node.printNode(), end=' ')
        self.DLR(node.left)
        self.DLR(node.right)

    def PathToLeaf_DLR(self, node, pathSoFar):
        if node == None:
            return

        if node.left == None and node.right == None:
            print('Path=', pathSoFar + [node.printNode()])
            return
        # print(node.printNode(), end=' ')
        self.PathToLeaf_DLR(node.left, pathSoFar + [node.printNode()])
        self.PathToLeaf_DLR(node.right, pathSoFar + [node.printNode()])

    def MaxDept(self, node):
        if node == None:
            return 0
        else:
            return 1 + max(self.MaxDept(node.left), self.MaxDept(node.right))

    def MinDept(self, node):
        if node == None:
            return 0
        else:
            return 1 + min(self.MinDept(node.left), self.MinDept(node.right))

    def BreadthFirstWalk(self):
        nodes = [self.root]
        while (nodes):
            node = nodes.pop(0)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            print(node.printNode(), end=' ')


def run():
    x = [1, 2, 3, 4, 1, 2, 3, 4]
    print(x[1:])
    print(x[:-1])
    x.remove(2)
    print(x)
    exit()
    mytree = Tree()
    root = mytree.GiveRootNode()
    print('DLR walk')
    mytree.DLR(root)
    mytree.PathToLeaf_DLR(root, [])
    print('Max dept is %d', mytree.MaxDept(root))
    print('Mix dept is %d', mytree.MinDept(root))
    print('Doing breadth first walk')
    mytree.BreadthFirstWalk()
    print('\ndone')
    return


def main():
    run()


if __name__ == "__main__":
    main()
