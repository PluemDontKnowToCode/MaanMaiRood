import math

class BPlusNode:
    def __init__(self, order):
        self.order = order
        self.values = []
        self.keys = []
        self.nextKey = None
        self.parent = None
        self.check_leaf = False
        pass

    def insert_at_leaf(self, leaf, value, key):
        if self.values == []:
            self.values = [value]
            self.keys = [[key]]
            return
        temp = self.values
        for i in range(len(temp)):
            if value == temp[i]:
                self.keys[i].append(key)
                break
            elif value < temp[i]:
                self.values = self.values[:i] + [value] + self.values[i:]
                self.keys = self.leys[:i] + [[key]] + self.keys[i:]
            elif i + 1 == len(temp): 
                self.values.append(value)
                self.keys.append([key])

class BplusTree:
    def __init__(self, order):
        self.root = BPlusNode(order)
        self.root.check_leaf = True

    def insert(self, value, key):
        value = str(value)
        node = self.search(value)
        node.insert_at_leaf(node, value, key)

        if len(node.values) == node.order:
            newNode = BPlusNode(node.order)
            newNode.check_leaf = True
            newNode.parent = node.parent

            mid = int(math.ceil(node.order / 2)) - 1
            newNode.values = node.values[mid + 1:]
            newNode.keys = node.keys[mid + 1:]
            newNode.nextKey = node.nextKey

            node.values = node.values[:mid + 1]
            node.keys = node.keys[:mid + 1]
            node.nextKey = newNode

            self.insert_in_parent(node, newNode.values[0], newNode)

    def search(self, value):
        node = self.root
        while not node.check_leaf:
            temp = node.values
            for i in range(len(temp)):
                if value == temp[i]:
                    node = node.keys[i + 1]
                elif value < temp[i]:
                    node = node.keys[i]
                elif i + 1 == len(node.values):
                    node = node.keys[i+ 1]
        return node
    
    def is_exist(self, value, key):
        node = self.search(value)
        for i , item in enumerate(node.values):
            if item == value:
                return key in node.keys[i]
        return False
    
    def insert_in_parent(self, n, value, ndash):
        if self.root == n:
            root = BPlusNode(n.order)
            root.values = [value]
            root.keys = [n, ndash]

            self.root = root
            n.parent = root
            ndash.parent = root
            return
        
        parentNode = n.parent
        temp = parentNode.keys

        for i in range(len(temp)):
            if temp[i] == n:
                parentNode.values = parentNode.values[:i]






