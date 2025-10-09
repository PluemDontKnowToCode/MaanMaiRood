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

    # === นี่คือฟังก์ชันที่แก้ไขแล้ว ===
    def add(self, data):
        current_data = int(data)
        if not self.root:
            self.root = Node(data)
            return

        # --- ส่วนที่ 1: การวน Loop เพื่อหาตำแหน่งและเก็บเส้นทาง (Path) ---
        path = []
        current = self.root # เริ่มจากรากของจริง แค่ครั้งเดียว
        while True: # ใช้ True loop แล้ว break ข้างในจะชัดเจนกว่า
            path.append(current)
            if current_data < current.data:
                if not current.left:
                    current.left = Node(data)
                    break
                current = current.left
            else: # สามารถใช้ else ได้เลย เพราะ AVL ไม่มีค่าซ้ำ
                if not current.right:
                    current.right = Node(data)
                    break
                current = current.right
        
        # --- ส่วนที่ 2: การย้อนรอย (Backtrack) เพื่อ Rebalance ---
        # Loop นี้จะทำงานย้อนหลังจากโหนดพ่อของใบใหม่ ขึ้นไปจนถึงราก
        for i in range(len(path) - 1, -1, -1):
            node = path[i]
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
            balance = self.getBalance(node)
            
            new_subtree_root = None

            # ตรวจสอบ 4 รูปแบบของการเสียสมดุล
            # Left Left Case
            if balance > 1 and current_data < node.left.data:
                new_subtree_root = self.rightRotate(node)
            # Right Right Case
            elif balance < -1 and current_data > node.right.data:
                new_subtree_root = self.leftRotate(node)
            # Left Right Case
            elif balance > 1 and current_data > node.left.data:
                node.left = self.leftRotate(node.left)
                new_subtree_root = self.rightRotate(node)
            # Right Left Case
            elif balance < -1 and current_data < node.right.data:
                node.right = self.rightRotate(node.right)
                new_subtree_root = self.leftRotate(node)

            # ถ้ามีการหมุนเกิดขึ้น ให้เชื่อมโหนดที่หมุนแล้วกลับเข้าต้นไม้
            if new_subtree_root:
                if i > 0:
                    parent = path[i-1]
                    if node == parent.left:
                        parent.left = new_subtree_root
                    else:
                        parent.right = new_subtree_root
                else: # ถ้าการหมุนเกิดขึ้นที่ root
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
        self.root = self._remove(self.root, data)

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
        root = node
        while root.left is not None:
            root = root.left
        return root
    
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