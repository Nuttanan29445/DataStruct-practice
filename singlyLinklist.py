class Node:
    def __init__(self, data=None):
        if(data is None):
            self.data = None
        else:
            self.data = data
        self.next = None

class linkList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    
    def __str__(self):
        p = self.head
        data = []
        while p:
            data.append(str(p.data))
            p = p.next
        return "->".join(data)
    
    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def size(self):
        node = self.head
        count = 0
        while node:
            count+=1
            node = node.next
        return count
            
    
    def isEmpty(self):
        return self.size() == 0
    
    def inSert(self, index, data):
        newNode = Node(data)
        node = self.head
        previous = None
        i = 0
        if(self.size() >= 1):     
            while node:
                if(i==index):
                    break
                previous = node
                node = node.next
                i+=1
            if(not previous):
                newNode.next = self.head
                self.head = newNode
            elif i == self.size():
                self.tail.next = newNode
                self.tail = newNode
            else:
                newNode.next = previous.next
                previous.next = newNode
        elif(self.size()==0):
            self.head = newNode
            self.tail = newNode
