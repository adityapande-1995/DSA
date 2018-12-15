#!python3
# A BST from scratch in python

class Node:
    def __init__(self,name,content = None):
        self.name = name
        self.content = content
        self.left = None
        self.right = None
        self.depth = 0

    def insert(self, other):
        other.depth += 1
        if other.content < self.content and not self.left:
            self.left = other
        elif other.content > self.content and not self.right:
            self.right = other
        elif other.content < self.content and self.left:
            self.left.insert(other)
        elif other.content > self.content and self.right:
            self.right.insert(other)


    # Equality check and hash for defaultdict in Graph class
    def __eq__(self,node2):
        return self.name == node2.name
    
    def __hash__(self):
        return id(self.name)
    
    # For printing and representing
    def __str__(self):
        return "N -"+ str(self.name)
    
    def __repr__(self):
        return "N -"+ str(self.name)

class BST:
    def __init__(self, node):
        self.root = node
    
    def insert(self, other):
        self.root.insert(other)

    def show_postorder(self, start):
        if start:
            self.show_inorder(start.left)
            self.show_inorder(start.right)
            print("Visited, value, depth: ", start, start.content, start.depth)

    def show_inorder(self, start):
        if start:
            self.show_inorder(start.left)

            print("Visited, value, depth: ", start, start.content, start.depth)

            self.show_inorder(start.right)
    
    def show_preorder(self, start, visited=[]):
        print("Visited, value, depth: ", start, start.content, start.depth)
        visited.append(start)

        if start.left and start.left not in visited:
            self.show_preorder(start.left,visited)
        
        if start.right and start.right not in visited:
            self.show_preorder(start.right,visited)

    def show_level_order(self, start):
        Q = [start]
        visited = [start]
        print("Visited, value, depth: ", start,start.content, start.depth)
        while len(Q) > 0:
            v = Q.pop(0)

            if v.left and v.left not in visited:
                Q.append(v.left)
                visited.append(v.left)
                print("Visited, value, depth: ", v.left,v.left.content, v.left.depth)
            
            if v.right and v.right not in visited:
                Q.append(v.right)
                visited.append(v.right)
                print("Visited, value, depth: ", v.right,v.right.content, v.right.depth)


# Main
alpha = Node("a", 10)
a = BST( alpha )
a.insert( Node("b", 5) )
a.insert( Node("c", 15) )
a.insert( Node("e", 17.5) )
a.insert( Node("f", 14) )
a.insert( Node("g", 7) )
a.insert( Node("h", 2) )
a.insert( Node("i", 1) )
a.insert( Node("j", 6) )
a.insert( Node("k", 8) )

print("Preorder traversal")
a.show_preorder( alpha )
print("\nLevel order traversal")
a.show_level_order( alpha )
print("\nInorder traversal")
a.show_inorder( alpha )
print("\nPostorder traversal")
a.show_postorder( alpha )

