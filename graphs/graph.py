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
        return "N -"+ str(self.name)
    
    def __repr__(self):
        return "N -"+ str(self.name)

class Graph:
    def __init__(self):
        self.g = defaultdict(list)
        self.edges = []

    def addNode(self, u, v, d=1): # Node 1, node 2, distance
        if not (v,d) in self.g[u]:
            self.g[u].append((v,d))
            self.g[v].append((u,d)) 
        else:
            print("Connection aready exists !")   

    def update_edges(self):
        self.edges = []
        for node in self.g:
            for (neighbour,distance) in self.g[node]:
                self.edges.append( (node, neighbour) )
    
    def show(self):
        print("Neighbours : ",self.g,"\n")
        print("Edges : ", self.edges)

    def DFS(self, current, visited=[]): # Depth first
        print("Visited node: ", current)
        visited.append(current)
        
        for child_node, distance in self.g[current]:
            if child_node not in visited:
                self.DFS(child_node, visited)

# Main

a = Graph()
a.addNode( Node("a"), Node("b") )
a.addNode( Node("a"), Node("c") )
a.addNode( Node("a"), Node("d") )
a.addNode( Node("b"), Node("e") )
a.addNode( Node("b"), Node("f") )
a.addNode( Node("b"), Node("g") )
a.addNode( Node("c"), Node("h") )
a.addNode( Node("f"), Node("h") )
a.update_edges() 

a.show()

a.DFS( Node("a") )
