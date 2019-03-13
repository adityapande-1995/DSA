#!python3
# Dijkstra's algorithm demo

def DJ(g,start_node):
    MAX = 1000
    # Initialize shortest distances
    shortest_distances = {}
    for node in g:
        if node != start_node:
            if node in g[start_node]:
                shortest_distances[node] = g[start_node][node]
            else:
                shortest_distances[node] = MAX
    
    # Initiale printing
    print("Start node: ", start_node)
    print("Initial shortest distances: ", shortest_distances)

    # Start iterating
    PQ = shortest_distances.copy()
    while len(PQ) != 0:
        current_node, _ = min(PQ.items(), key= lambda x:x[1])
        print("** Current node :", current_node)

        # Iterate over neighbours of cuurent node which are in PQ
        for next_node, increment_dist in g[current_node].items():
            if next_node in PQ:
                print("Checking neighbour :", next_node)
                # Perform relaxation
                new_dist = shortest_distances[current_node] + increment_dist
                old_dist = shortest_distances[next_node]
                if new_dist < old_dist:
                    shortest_distances[next_node] = new_dist

        # Pop current node from PQ
        PQ.pop(current_node)

        # Print updated shortest distances
        print(shortest_distances)


if __name__ == "__main__":
    graph = {
            'a' : {'b':1 , 'f':5}, 
            'b' : {'a':1 , 'c':2 , 'd':3}, 
            'c' : {'f':2 , 'b':2, 'd':0.5},
            'd' : {'c':0.5 , 'b':3 , 'e':1},
            'e' : {'d':1},
            'f' : {'a':5 , 'c':2}
            }
    DJ(graph, 'a')

    

