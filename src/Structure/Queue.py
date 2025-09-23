class Queue:
    def __init__(self):
        self.items = []
        return
    
    def enQueue(self, i):
        self.items.append(i)
        return
    
    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)