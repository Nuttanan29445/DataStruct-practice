class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
class DoublyLinklist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.previous = None 
        self.countRemove = 0
    
    def __str__(self):
        p = self.head
        data = []
        while p:
            data.append(str(p.data))
            p = p.next
        return "->".join(data)
    
    def Tail(self):
        return self.tail.data
    
    def str_reverse(self):
        p = self.head
        data=[]
        while p:
            data.append(str(p.data))
            p = p.next
        data1 = data[::-1]
        return "->".join(data1)
    
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
        self.previous = None
        i = 0
        if(self.size() >= 1):     
            while node:
                if(i==index):
                    break
                self.previous = node
                node = node.next
                i+=1
            if(not self.previous):
                newNode.next = self.head
                self.head = newNode
            else:
                if(i==self.size()):
                    self.tail.next = newNode
                    self.tail = newNode
                else:
                    newNode.next = self.previous.next
                    self.previous.next = newNode
        elif(self.size()==0):
            self.head = newNode
            self.tail = newNode
    
    def remove(self, data):
        removeNode = Node(data)
        p = self.head
        self.previous = None
        self.countRemove = 0
        while(p):
            if(p.data==removeNode.data):
                if(not self.previous):
                    self.head = p.next
                else:
                    if(self.countRemove+1 == self.size()):
                        self.previous.next = None
                        self.tail = self.previous
                    else:
                        self.previous.next = p.next
                break
            self.previous = p
            p = p.next
            self.countRemove+=1
        
        
    def indexRemove(self):
        return self.countRemove