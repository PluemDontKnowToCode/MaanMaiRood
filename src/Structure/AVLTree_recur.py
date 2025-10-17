from Helper.formula import *
class AVLNode:
	def __init__(self, data , left = None, right = None):
		self.data = data
		self.left = None if left is None else left
		self.right = None if right is None else right
		self.height = self.setHeight()

	def __str__(self):
		return str(self.data)
	
	def setHeight(self):
		a = self.getHeight(self.left)
		b = self.getHeight(self.right)
		self.height = 1 + max(a,b)
		return self.height
	
	def getHeight(self,node):
		return -1 if node == None else node.height
	
	def balanceValue(self):
		return int(self.getHeight(self.left)) - int(self.getHeight(self.right))
    
class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, data):
        self.root = self._add(self.root, data)
        self.size -= 1

    def _add(self, root, data):
        if root is None:
            return AVLNode(data)
        if int(data) < int(root.data):
            root.left = self._add(root.left, data)
        else:
            root.right = self._add(root.right, data)
        root = self.rebalance(root)
        return root

    def rebalance(self, x):
        if x == None:
            return x
        balance = x.balanceValue()

        if balance <= -2:
            if x.right.balanceValue() == 1:
                x.right = self.leftRotate(x.right)
            x = self.rightRotate(x)
        elif balance >= 2:
            if x.left.balanceValue() == -1:
                x.left = self.rightRotate(x.left)
            x = self.leftRotate(x)
        x.setHeight()
        return x

    def leftRotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        x.setHeight()
        y.setHeight()
        return y

    def rightRotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        x.setHeight()
        y.setHeight()
        return y

    def _printTree(self, node, level = 0):
        if node != None:
            self._printTree(node.left, level + 1)
            print(f"{node}")
            self._printTree(node.right, level + 1)

    def printTree(self):
        self._printTree(self.root)
        
    def compare(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        
        return (
            node1.data == node2.data and
            self.compare(node1.left, node2.left) and
            self.compare(node1.right, node2.right)
        )	
    
    def remove(self, data):
        self.root = self._remove(self.root, data)
        self.size -= 1

    def _remove(self, node, data):
        if node is None:
            return None
        if data < node.data:
            node.left = self._remove(node.left, data)
        elif data > node.data:
            node.right = self._remove(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.get_successer(node.right)
            node.data = temp.data
            node.right = self._remove(node.right, temp.data)
        return self.rebalance(node)
    
    def get_successer(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def preorder(self, focus, List):
        # Root → Left → Right
        if focus is not None:
            List.append(focus.data)
            if focus.left is not None:
                self.preorder(focus.left ,List)
            if focus.right is not None:
                self.preorder(focus.right ,List)
        return List
    
    def inorder(self):
        if self.root == None:
            return None
        op = []
        return self._inorder(self.root, op)
    
    def _inorder(self, focus, List):
        # Left → Root → Right
        if focus.left is not None:
            self._inorder(focus.left, List)
        List.append(focus.data)
        if focus.right is not None:
            self._inorder(focus.right, List)
        return List
    
    def postorder(self, focus, List):
        #Left → Right → Root
        if focus.left is not None:
            self.postorder(focus.left, List)
        if focus.right is not None:
            self.postorder(focus.right, List)
        List.append(focus.data)
        return List
    
    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node == None:
            return None 
        
        if node.data == data:
            return node
        if node.data > data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)
        
    def update(self):
        self._update(self.root, 0)

    def _update(self, focus, value):
        if focus is None:
            return None
        if focus.left is not None:
            self._update(focus.left, value)
        focus.data.number = Formula.triangular_accumulate(focus.data.number, value)
        if focus.right is not None:
            self._update(focus.right, value)