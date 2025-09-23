class Stack:
    def __init__(self, data = None):
        if data is not None:
            self.items = data
        else:
            self.items = []
    
    def push(self, value):
        if not value is None:
            self.items.append(value)
        return
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
    
    def inverse(self):
        self.items = self.items[::-1]