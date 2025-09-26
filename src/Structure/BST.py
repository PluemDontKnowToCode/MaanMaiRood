from Queue import Queue

class BST:
    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.__left =  self.__right = None

        @property
        def left(self): return self.__left

        @property
        def right(self): return self.__right

        @left.setter
        def left(self, node):
            if(isinstance(node, BST.TreeNode)):
                self.__left = node

        @right.setter
        def right(self, node):
            if(isinstance(node, BST.TreeNode)):
                self.__right = node

        def __str__(self):
            return str(self.data)
        
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = BST.TreeNode(data)
        if self.root is None:
            self.root = newNode
        else:
            self.traverse(self.root, newNode)
        return self.root
    
    def traverse(self,focus, node):
        if node.data == focus.data:
            return 0
        if node.data > focus.data:
            if focus.right is None:
                focus.right = node
                return 0
            else:
                return self.traverse(focus.right ,node)
        else:
            if focus.left is None:
                focus.left = node
                return 0
            else:
                return self.traverse(focus.left ,node)
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    def preorder(self, focus, List):
        # Root → Left → Right
        if focus is not None:
            List.append(focus.data)
            if focus.left is not None:
                self.preorder(focus.left ,List)
            if focus.right is not None:
                self.preorder(focus.right ,List)
        return List
    def inorder(self, focus, List):
        # Left → Root → Right
        # 1 4 5 10 20 
        
        if focus.left is not None:
            self.inorder(focus.left, List)
            
        List.append(focus.data)
        if focus.right is not None:
            self.inorder(focus.right, List)
        return List
    def postorder(self, focus, List):
        #Left → Right → Root
        if focus.left is not None:
            self.postorder(focus.left, List)
        if focus.right is not None:
            self.postorder(focus.right, List)
            
        List.append(focus.data)
        return List
    
    def BFS(self, focus,queue, List):
        if focus is not None:
            List.append(focus.data)
            
            if focus.left is not None:
                queue.enQueue(focus.left)
            if focus.right is not None:
                queue.enQueue(focus.right)
            
            if queue.isEmpty():
                return List
            
            deq = queue.deQueue()
            self.BFS(deq, queue,List)
        
        return List
    def ListToStr(self, List):
        return ' '.join(map(str, List))
