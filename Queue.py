class Queue:
    def __init__(self, list = []):
        self.items = list
    
    def enQueue(self, i):
        self.items.append(i)
    
    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def getItems(self):
        return self.items
    
    def __str__(self):
        return " ".join(str(x) for x in self.items)