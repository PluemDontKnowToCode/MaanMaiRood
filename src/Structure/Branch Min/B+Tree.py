# keys จะเก็บ key -> เลขห้อง(มั้ง)
# data จะเก็บ datum -> ชื่อคนในห้องนั้น Ex. Guest#0, Guest#111 (มั้ง)
# โดยการหาจะหาจากตัวแปร key(เลขห้อง) | data มีหน้าที่เเค่เก็บข้อมูลนั้นเฉยๆ

# -------------------Plan-------------------
# 1.) Delete -> ทำให้ datum เเละ key ใน leaf node หาย -> ชื่อคนในห้องนั้นหาย -> ห้องว่าง -> ลบห้อง  
# 2.) บรรทัดที่ 113 
# 4.) บรรทัดที่ 148 น่าจะเเก้ให้หาได้เเบบ binary Tree (greedy เลือกซ้ายขวาได้ โดยใช้ key เลือก)
# 3.) ขยันก็ทำ A-(B++) Tree เเม่งชี้ไปข้างหลังได้ด้วย
# *** vibe เเล้วช่วยกรุณาเขียน comment ด้วยว่ามันทำอะไรลงไป !!! (เป็นไปได้ใส่ตัวอย่าง เเละ case ไว้ใน main())


# -------------------Rule-------------------
# Each node except root can have a maximum of M children and at least ceil(M/2) children.
# Each node can contain a maximum of M - 1 keys and a minimum of ceil(M/2) - 1 keys.
# The root has at least two children and atleast one search key.
# While insertion overflow of the node occurs when it contains more than M - 1 search key values.
# (แนะนำให้ช่างมันก่อน ค่อยมาทำความเข้าใจทีหลัง)


class Node:
    def __init__(self,order):
        self.order = order          # ต่อจากนี้ attribute ถ้าเป็น sigular(datum) -> 1 
        self.keys = []              # ถ้าเป็น plural(-s, data) -> list[]

class LeafNode(Node):       # class เก็บข้อมูลเเละตัวชี้
    def __init__(self,order):
        super().__init__(order)
        self.data = []              # เก็บข้อมูล
        self.next = None            # ไว้ชี้ตัวต่อไป 

class InternalNode(Node):   #  class ระหว่างกลาง leaf กับ root
    def __init__(self,order):
        super().__init__(order)
        self.children = []          # เก็บลูก




class B_PlusTree:           # class ใหญ่
    def __init__(self, order):
        self.order = order          # ใส่ max capacity ของ Node
        self.root = LeafNode(order) # root 
        self.first_leaf = None      # leaf ล่างซ้ายสุด (น้อยสุด)


    def search(self,find):
        node = self.root
        # กรณีที่ยังไปไม่ถึง leaf
        while isinstance(node, InternalNode):   
            i = 0
            while i < len(node.keys) and find >= node.keys[i]:      # ค้นหาใน list internal Node  
                i += 1
            node = node.children[i]
        
        # เมื่อถึง leaf node เเล้ว
        for i,k in enumerate(node.keys):        # ค้นหาใน list leaf Node  
            if k == find:
                return node.data[i]
        
        print(f"Cannot find {find} in Hotel")
        return None


    def insert(self, key, data):
        leaf = self._find_leaf(self.root, key)  # หาว่าจะใส่ข้อมูลที่ leaf node ไหน
        if leaf is self.root :
            self.first_leaf = leaf

        self._insert_in_leaf(leaf, key, data)   # เริ่มหา index ที่ data กับ key ควรอยู่ใน list เเละใส่ไว้ด้วยกัน
        if len(leaf.keys) >= self.order :       # ถ้าเกิน capacity-1  เพราะแต่ละ node มีได้แค่ M-1 keys
            self._split_leaf(leaf)                  # ถ้าเกินต้องแบ่งต้นไม้ เป็น 2 ส่วน


    def _find_leaf(self, node, find):
        if isinstance(node, LeafNode):                              # คืนค่า leafnode ถ้าเป็น leafnode
            return node
        
        i = 0
        while i < len(node.keys) and find > node.keys[i]:           # ค้นหาใน list InternalNode  
            i += 1
        return self._find_leaf(node.children[i], find)
    
        
    # node ต้องเป็น LeafNode แล้ว
    def _insert_in_leaf(self, leaf : LeafNode, key, data):    
        i = 0
        while i < len(leaf.keys) and key > leaf.keys[i]:            # หาที่ๆมันควรอยู่ Ex. 0 2 จะเติม 1 จะได้ i=1 เเล้วค่อยออกจาก while เพื่อไปเติมข้างล่าง
            i+=1

        leaf.keys.insert(i, key)                                    # ใส่ค่า key, data ใน attribute list[] keys, data ของ LeafNode 
        leaf.data.insert(i, data)


    def _split_leaf(self, leaf):
        new_leaf = LeafNode(self.order)
        mid = (self.order + 1) // 2             # เเบ่งครึ่ง

        # เราจะให้ new_leaf เก็บข้อมูลที่มีค่า key มากกว่าา
        # เริ่มย้ายข้อมูล keys,data (ย้ายครี่งหลัง mid มาใส่ไว้ในนี้)
        new_leaf.keys = leaf.keys[mid:]           
        new_leaf.data = leaf.data[mid:]

        # ลบข้อมูลครึ่งหลังเดิม (เก็บถึงเเค่ครึ่งเเรก)
        leaf.keys = leaf.keys[:mid]
        leaf.data = leaf.data[:mid]             

        # แทรก new_leaf ระหว่างกลาง leaf -> new_leaf -> leaf.next(เดิม)
        new_leaf.next = leaf.next               
        leaf.next = new_leaf

        # ต้องใส่ key ใหม่ไป parent 
        new_key = new_leaf.keys[0]              # new_key : pointer ที่ชี้ไป index เเรกของ key[]
        self._insert_in_parent(leaf, new_key, new_leaf)

    
    # เพิ่ม new_node โดยการหา parent ของ node เเลัวเพิ่ม key กับ child ใน parent list[]
    # new_node จะมี keys ทั้งหมด(ยกเว้นตัวเเรกที่เท่ากัน)สูงกว่า key เสมอ
    def _insert_in_parent(self, node, key, new_node):
        if node == self.root:                   # กรณีอยากเพิ่ม parent ตรง root (เพิ่มบนสุด) 
            new_root = InternalNode(self.order)         # สร้าง root ใหม่
            new_root.keys = [key]                       # เก็บ key    |      new-root
            new_root.children = [node, new_node]        # เก็บ ลูก    ->  node _| |_ new_node
            self.root = new_root                        # change root   
            return
        
        # กรณี InternalNode
        parent = self._find_parent(self.root, node)
        # แทรก key, child ใน Internal parent (parent -> InternalNode)
        i = 0
        # ทำไมไม่ใช้ append wa 
        while i < len(parent.children) and parent.children[i] is not node:    # ไล่ไปให้เจอตัวท้ายของ list 
            i += 1
        parent.keys.insert(i, key)              # เพิ่มข้อมูลตอนท้าย
        parent.children.insert(i+1, new_node)

        if len(parent.children) > self.order:   # ถ้าเกิน capacity เพราะเเต่ละ node เก็บได้มากสุด M children
            self._split_internal(parent)


    def _split_internal(self, internal):
        new_internal = InternalNode(self.order)
        mid = self.order // 2
        mid_key = internal.keys[mid]            # เก็บ key[mid] ไว้ก่อนเดี๋ยวหาย จะได้นำขึ้นไปอยู่บน parent node

        # keys, children
        new_internal.keys       = internal.keys[mid+1:]   # ที่ต้อง mid+1 เพราะตัว keys[mid] ต้องถูก promote ขึ้นไปบน parent (พลาดมาละ)
        new_internal.children   = internal.children[mid+1:]

        internal.keys       = internal.keys[:mid]
        internal.children   = internal.children[:mid+1]

        # update parent node
        self._insert_in_parent(internal, mid_key, new_internal)


    # หา parent ของ child นั้นโดยใช้ DFS 
    def _find_parent(self, node, child):
        if isinstance(node, LeafNode):          # เมื่อ dfs ลงมาถึง leaf (ล่างสุด) ไม่เจอก็ให้ return None
            return None
        
        for c in node.children:
            if c is child:
                return node
            
            # กรณีที่ใน InternalNode นั้นไม่มี child ตัวนั้นก็ให้ลงไป check InternalNode ไปเรื่อยๆ
            parent = self._find_parent(c, child)    
            if parent:                          # ถ้าเจอก็ return ไปเรื่อยๆ
                return parent
            
        # print(f"Cannot find {child.keys} parent node in Hotel")
        return None
    
    



        
def main():
    NTree = B_PlusTree(3)
    NTree.insert(10, "A")
    NTree.insert(20, "B")
    NTree.insert(5, "C")
    NTree.insert(6, "D")
    NTree.insert(12, "E")
    NTree.insert(17, "E")
    NTree.insert(18, "E")
    NTree.insert(19, "E")
    NTree.insert(25, "E")
    NTree.insert(30, "E")
    NTree.insert(100, "E")
    NTree.insert(21, "E")
    # NTree.insert(2, "E")
    # NTree.insert(17, "E")

    print(NTree.search(6))   # 👉 ได้ "D"
    # print(NTree.search(15))  # 👉 None   
    print(NTree.search(12))     

    
    print_bplustree(NTree.root)


    draw_leaf_links(NTree.first_leaf)


def print_bplustree(node, level=0): # vibe มาไม่ต้องสนใจ
    indent = "    " * level
    if node is None:
        return

    if hasattr(node, "children"):  # Internal node
        print(f"{indent}Internal: {node.keys}")
        for child in node.children:
            print_bplustree(child, level+1)
    else:  # Leaf node
        print(f"{indent}Leaf: {list(zip(node.keys, node.data))}")


def draw_leaf_links(first_leaf):
    """พิมพ์ leaf linked list"""
    print("\nLeaf linked list:")
    cur = first_leaf
    while cur:
        print("{" + ", ".join(str(k) for k in cur.keys) + "}", end="")
        if cur.next:
            print(" → ", end="")
        cur = cur.next
    print()




main()



