#!python3
from collections import defaultdict

class Node:
    def __init__(self,name,content = None):
        self.name = name
        self.content = content

    # Equality check and hash for defaultdict in Graph class
    def __eq__(self,node2):
        return self.name == node2.name
    
    def __hash__(self):
        return id(self.name)
    
    # For printing and representing
    def __str__(self):
        return "Node -"+ str(self.name)
    
    def __repr__(self):
        return "Node -"+ str(self.name)

class Graph:
    def __init__(self):
        self.g = defaultdict(list)
        self.edges = []
    
    def addNode(self, u, v):
        if not v in self.g[u]:
            self.g[u].append(v)
            self.g[v].append(u) 
        else:
            print("Connection aready exists !")       
    
    def update_edges(self):
        self.edges = []
        for node in self.g:
            for neighbour in self.g[node]:
                self.edges.append( (node, neighbour) )
    
    def show(self):
        print("Neighbours : ",self.g,"\n")
        print("Edges : ", self.edges)

    def DFS(self, stack=None):
        pass

        
       

# Main
a = Graph()
a.addNode( Node("a"), Node("b") )
a.addNode( Node("a"), Node("c") )
a.addNode( Node("a"), Node("e") )
a.addNode( Node("b"), Node("d") )
a.addNode( Node("b"), Node("f") )
a.addNode( Node("c"), Node("g") )
a.addNode( Node("e"), Node("f") )

a.update_edges() 
a.show()
