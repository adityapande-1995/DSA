#!PYTHON3

class Node:
    def __init__(self, num):
        self.content = num
        self.prev = None
        self.next = None
    
    def addNext(self, other):
        self.next = other
        other.prev = self
    
    def addPrev(self,other):
        self.prev = other
        other.next = self

class LL:
    def __init__(self, head):
        self.head = head
        self.last = head
        self.length = 1
    
    def pushback(self,node):
        self.last.addNext(node)
        self.last = node
        self.length += 1

    def pushfront(self,node):
        self.head.addPrev(node)
        self.head = node
        self.length += 1

    def insert_after(self, other, index0):
        temp = self.head
        for i in range(index0):
            temp = temp.next
        other.addNext(temp.next)
        temp.addNext(other)
        self.length += 1
    
    def get(self, index):
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

    def delete(self, index):
        if index !=0 and index != (self.length -1):
            temp = self.head
            for i in range(index):
                temp = temp.next
            temp.prev.addNext(temp.next)
            self.length -= 1
    
    def show(self):
        i = 0
        temp = self.head
        while temp:
            print("Node, index : ",temp.content,i)
            temp = temp.next
            i += 1
        print("Head node : ", self.head.content)
        print("Last node : ", self.last.content)
        print("Length : ", self.length)

# Main
a = LL( Node("A") )
a.pushback( Node("B") )
a.pushback( Node("C") )
a.insert_after( Node(100), 1)
a.pushback( Node("E") )
a.show()
print("\nFurther operations")
a.delete(3)
a.pushfront( Node("Alpha") )
a.show()

