#!python3
# Bellman Ford algorithm
# This handles negative weights

from math import inf

def BF(graph, nodes):
    # Initialize shortest distances
    shortest_distances = {n:inf for n in nodes}
    shortest_distances[1] = 0

    print("Run 0 : ",shortest_distances)

    # Iterate n-1 times
    for i in range(len(nodes) - 1):
        # Iterate over each edge
        for edge, increment_dist in graph.items():
            new_dist = shortest_distances[ edge[0] ] + increment_dist
            old_dist = shortest_distances[ edge[1] ]
            if new_dist < old_dist:
                shortest_distances[ edge[1] ] = new_dist

        # Print updates
        print("Run ", i+1, " : ",shortest_distances)


if __name__ == "__main__":
    nodes = [1,2,3,4,5,6,7]
    graph = {(1,2):6, (1,3):5, (1,4):5, (2,5):-1, (3,2):-2, (3,5):1, 
            (4,3):-2, (4,6):-1, (5,7):3, (6,7):3 }
    BF(graph, nodes)


