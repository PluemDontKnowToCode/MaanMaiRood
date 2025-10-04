class Node:
    def __init__(self,order):
        self.order = order
        self.key = [] 


class LeafNode(Node):       # class เก็บข้อมูลเเละตัวชี้
    def __init__(self, order):
        self.data = []              # เก็บข้อมูล
        self.next = None            # ไว้ชี้ตัวต่อไป 

class InternalNode(Node):   #  class ระหว่างกลาง leaf กับ root
    def __init__(self, order):
        self.children = []          # เก็บลูก




class B_PlusTree:           # class ใหญ่
    def __init__(self, order):
        self.order = order          # ใส่ max capacity ของ Node
        self.root = LeafNode(order) # root 


    def search(self,find):
        node = self.root
        while isinstance(node, InternalNode):   # ยังไปไม่ถึง leaf
            i = 0
            while i < len(node.key) and find >= node.key[i]:   # ค้นหาใน list internal Node  
                i += 1
            node = node.children[i]
        
        # เมื่อถึง leaf node เเล้ว
        for i,k in enumerate(node.key):         # ค้นหาใน list leaf Node  
            if k == find:
                return node.values[i]
        
        print(f"Cannot find {find} in Hotel")
        return None


    def insert(self, key, value):
        leaf = self._find_leaf(self.root, key)  # หาว่าจะใส่ข้อมูลที่ leaf node ไหน
        self._insert_in_leaf(leaf, key, value)  # เริ่มใส่ข้อมูล value กับ key ไว้ด้วยกัน
        if len(leaf.key) >= self.order :        # ไม่ให้เกิน capacity
            self._split_leaf(leaf)              # ถ้าเกินต้องแบ่งต้นไม้ เป็น 2 ส่วน

        def _find_leaf(self, ):
            pass

        def _insert_in_leaf(self, );
            pass