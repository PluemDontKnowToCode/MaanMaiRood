class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.height = 1
    def __str__(self):
        return str(self.data)

class AVLTree:
    def __init__(self):
        self.root = None

    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rightRotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        return x

    def leftRotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y


    def add(self, data):
        current_data = int(data)
        if not self.root:
            self.root = Node(data)
            return

        path = []
        current = self.root 
        while True: 
            path.append(current)

            if current_data < current.data:
                if not current.left:
                    current.left = Node(data)
                    break
                current = current.left
            else: 
                if not current.right:
                    current.right = Node(data)
                    break
                current = current.right

        self.rebalance(path,1,data)

        
    def rebalance(self, path, mode, data=None):
        for i in range(len(path) - 1, -1, -1):
            node = path[i]
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
            balance = self.getBalance(node)
            
            new_subtree_root = None

            if balance > 1:
                if (mode and data < node.left.data) or (not mode and self.getBalance(node.left) >= 0):
                    new_subtree_root = self.rightRotate(node)   # LL
                else:
                    node.left = self.leftRotate(node.left)      # LR
                    new_subtree_root = self.rightRotate(node)

            elif balance < -1:
                if (mode and data > node.right.data) or (not mode and self.getBalance(node.right) <= 0):
                    new_subtree_root = self.leftRotate(node)    # RR
                else: # RL
                    node.right = self.rightRotate(node.right)   # RL
                    new_subtree_root = self.leftRotate(node)


            if new_subtree_root:
                if i > 0:
                    parent = path[i-1]
                    if node == parent.left:
                        parent.left = new_subtree_root
                    else:
                        parent.right = new_subtree_root
                else:       # กรณีที่ rebalance ที่มีการย้าย root
                    self.root = new_subtree_root


    def _printTree(self, node, level = 0):
        if node != None:
            self._printTree(node.left, level + 1)
            print(f"{str(node)}")
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
        current_data = int(data)
        if not self.root:
            print("\nNo Room\n")
            return 
        
        path = []
        current = self.root
        parent = None
        
        while current and current.data != current_data: # หาทางไปเรื่อยๆ จนกว่าจะตรงค่า หรือ ถึง leaf node
            parent = current
            path.append(parent)
            if current_data < current.data:
                current = current.left
            else:
                current = current.right

        if not current: # ถ้าหาไม่เจอ
            print(f"Cannot find data {current_data}")
            return

        elif not current.left or not current.right: # โหนดที่จะลบมีลูก 1 
            child = current.left if current.left else current.right
                
            if not parent: # กรณีลบ root
                self.root = child
            elif current == parent.left:
                parent.left = child 
            else:
                parent.right = child 
        
        else:   # โหนดที่จะลบมีลูก 2
            successor_parent = current
            successor = current.right
            
            path.append(successor_parent) 
            
            while successor.left: # หา successor ที่น้อยที่สุดฝั่งขวา
                path.append(successor)
                successor_parent = successor
                successor = successor.left
            
            current.data = successor.data # สลับค่า
            
            if successor == successor_parent.left:  # ลบ successor 
                successor_parent.left = successor.right # ยังไงก็มีแค่ทางขวา ถ้า successor มีลูก
            else: 
                successor_parent.right = successor.right

        self.rebalance(path, 0) 

    
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
        
    def update(self, value):
        self._update(self.root, value)

    def _update(self, focus, value):
        if focus is None:
            return None
        if focus.left is not None:
            self._update(focus.left, value)
        focus.data.number += value
        if focus.right is not None:
            self._update(focus.right, value)