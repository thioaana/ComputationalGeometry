class Node :
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.height = 1

    def getKey(self):   return self.key
    def getValue(self): return self.value
    def getParent(self):return self.parent
    def getLeft(self):  return self.left
    def getRight(self): return self.right
    def getHeight(self): return self.height
    def setParent(self, n):  self.parent = n
    def setLeft(self, n):  self.left = n
    def setRight(self, n):  self.right = n
    def setKey(self, k): self.key = k
    def setValue(self, v): self.value = v
    def setHeight(self, h): self.height = h

class BSTTree:
    def __init__(self, ff):
        self.root = None
        self.orderFunc = ff

    def getRoot(self): return self.root

    # Helper function to find minimum key node in subtree rooted on currNode
    def _getSuccessor(self, currNode):
        while currNode.getLeft() :
            currNode = currNode.getLeft()
        return currNode

    # Helper function to find maximum key node in subtree rooted on currNode
    def getMaximumKey(self, currNode):
        while currNode.getRight() :
            currNode = currNode.getRight()
        return currNode

    # Input : A node of the Tree and a key
    # Output: True if key exist in the Tree and the node with node.key = key.
    #         False if key does not exist in the Tree and the parent node of the key if the key is going to be inserted in the Tree.
    def _Find(self, curNode, k):
        if self.orderFunc(curNode.getKey(), k) == 0:#curNode.getKey() == k :
            return True, curNode
        if self.orderFunc(curNode.getKey(), k) == -1:#curNode.getKey() < k :
            if curNode.getRight() is not None : return self._Find(curNode.getRight(), k)
            else :                              return False, curNode
        else :
            if curNode.getLeft() is not None :   return self._Find(curNode.getLeft(), k)
            else :                              return False, curNode

    # Input : key and value of a new Node
    # Output: Inserts a new Node in the Tree and updates all the pointers
    #         In case the key of the new node exists in the Tree, inserts nothing.
    def insert(self, k, v):
        newNode = Node(k, v)
        if self.root is None:
            self.root = newNode
            return
        (found, parent) = self._Find(self.root, newNode.getKey())
        if not found :
            newNode.setParent(parent)
            if self.orderFunc(parent.getKey(), newNode.getKey()) == -1 : parent.setRight(newNode)
            else : parent.setLeft(newNode)

    # Input : Key of the node to be deleted
    # Output: True if the node is found in the Tree and deleted and the parent node of the deleted node
    #         False if the node is not found in the Tree, and None
    def delete(self, key):
        # pointer to the parent node of current node
        parent = None

        # Start with root node
        currNode = self.root

        # search key in BST
        while currNode and currNode.getKey() != key :
            parent = currNode   #update parent
            if self.orderFunc(key, currNode.getKey()) == -1 :
                currNode = currNode.getLeft()
            else :
                currNode = currNode.getRight()

        # if key is not in the Tree just return
        if currNode is None :
            return False, None

        # Case 1: Node to be deleted has no children. It is a leaf
        if currNode.getLeft() is None and currNode.getRight() is None :
            if currNode == self.root :  # if the node is the root of the Tree
                self.root = None
            else :
                if parent.getLeft() == currNode :
                    parent.setLeft(None)
                else :
                    parent.setRight(None)


        # Case 2: Node to be deleted has two children.
        elif currNode.getLeft() and currNode.getRight() :
            # Find the successor node
            successor = self._getSuccessor(currNode.getRight())
            succKey, succValue = successor.getKey(), successor.getValue()
            # Recursively delete successor. The successor has most only right-child.
            result = self.delete(succKey) # Returns True because val exists in the Tree
            currNode.setKey(succKey)
            currNode.setValue(succValue)

        # Case 3: Node to be deleted has only one child.
        else :
            if currNode.getLeft() :
                child = currNode.getLeft()
            else :
                child = currNode.getRight()
            if currNode == self.root :
                self.root = child
                self.root.setParent(None)
            else :
                if parent.getLeft() == currNode :
                    parent.setLeft(child)
                else :
                    parent.setRight(child)
                child.setParent(parent)

        return True, currNode.getParent()

class BSTBalancedTree(BSTTree):
    def __init__(self, orderfunc):
        BSTTree.__init__(self, orderfunc)

    # Helper function to find the Hight of a node, used in balancing the Balanced BST
    def _getNodeHeight(self,  n):
        if n is None : return 0
        if n.getLeft() is None and n.getRight() is None :
            return 1
        else :
            return 1 + max(self._getNodeHeight(n.getLeft()), self._getNodeHeight(n.getRight()))

    def _Rebalance(self, n):
        parent = n.getParent()
        leftBranchHeight  = self._getNodeHeight(n.getLeft())
        rightBranchHeight = self._getNodeHeight(n.getRight())
        if leftBranchHeight > rightBranchHeight + 1 :
            self._RebalanceRight(n)
        if rightBranchHeight > leftBranchHeight + 1 :
            self._RebalanceLeft(n)
        # self.AdjustHeight(n)
        if parent is not None :
            self._AdjustHeight(parent)
            self._Rebalance(parent)

    def _AdjustHeight(self, n) :
        if n == None : return
        leftBranch = n.getLeft()
        rightBranch = n.getRight()
        if leftBranch and rightBranch :
            n.setHeight(1 + max(leftBranch.getHeight(), rightBranch.getHeight()))
        elif leftBranch is None and rightBranch :
            n.setHeight(1 + rightBranch.getHeight())
        elif leftBranch  and rightBranch is None:
            n.setHeight(1 + leftBranch.getHeight())
        else :
            n.setHeight(1)

    def _RebalanceRight(self, n):
        m = n.getLeft()
        if self._getNodeHeight(m.getRight()) > self._getNodeHeight(m.getLeft()) :
            self._RotateLeft(m)
        self._RotateRight(n)

    def _RebalanceLeft(self, n):
        m = n.getRight()
        if self._getNodeHeight(m.getLeft()) > self._getNodeHeight(m.getRight()) :
            self._RotateRight(m)
        self._RotateLeft(n)

    def _RotateRight(self, n):
        # Saves in memory
        nParent = n.getParent()
        y = n.getLeft()
        # Rotate
        n.setLeft(y.getRight())
        y.setRight(n)
        # Define new parents
        if n.getLeft()  : n.getLeft().setParent(n)
        y.setParent(n.getParent())
        n.setParent(y)
        if nParent :
            if nParent.getLeft() == n :
                nParent.setLeft(y)
            else :
                nParent.setRight(y)
        else :
            self.root = y
        # Update heights
        self._AdjustHeight(n)
        self._AdjustHeight(y)
        if nParent : self._AdjustHeight(nParent)

    def _RotateLeft(self, n):
        # Saves in memory
        nParent = n.getParent()
        y = n.getRight()
        # Rotate
        n.setRight(y.getLeft())
        y.setLeft(n)
        # Define new parents
        if n.getRight()  : n.getRight().setParent(n)
        y.setParent(n.getParent())
        n.setParent(y)
        if nParent :
            if nParent.getLeft() == n:
                nParent.setLeft(y)
            else:
                nParent.setRight(y)
        else :
            self.root = y
        # Update heights
        self._AdjustHeight(n)
        self._AdjustHeight(y)
        if nParent : self._AdjustHeight(nParent)

    # Input : Key of the node to be deleted
    # Output: True if the node is found in the Tree and deleted
    #         False if the node is not found in the Tree
    def insert(self, k, v):
        BSTTree.insert(self, k, v)
        found, newNode = self._Find(self.root, k)
        if found :
            self._Rebalance(newNode)

    def delete(self, key):
        (deleted, parent) = BSTTree.delete(self, key)
        if deleted :
            self._AdjustHeight(parent)
            if parent : self._Rebalance(parent)
            else : self._Rebalance(self.root)

def ff(x, y):
    if x == y  : return 0
    elif x < y : return -1
    else : return 1

if __name__ == "__main__" :
    myTree = BSTBalancedTree(ff)

    # keys = [15, 10, 20, 8, 12, 16]
    keys = [50, 30, 20, 40, 70, 60, 80]
    for k in keys:
        myTree.insert(k, k)
    myTree.delete(20)
    myTree.delete(30)
    myTree.delete(50)
    myTree.insert(6, 6)
#     myTree.insert(8, 8)
#     myTree.insert(5, 5)
#     myTree.insert(4, 4)
#     myTree.insert(6, 6)
#     myTree.insert(1, 1)
#     myTree.insert(2, 2)
#     myTree.delete(4)
#     myTree.delete(1)
#     myTree.delete(5)
#     myTree.delete(6)
#     myTree.delete(8)
#     myTree.delete(2)
#     print(5)