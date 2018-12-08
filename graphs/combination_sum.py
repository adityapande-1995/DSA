#!python3
import numpy as np

nums = [1,2,5]
mysum = 10
# nums = [1,2,3,4,5]
# mysum = 20

UPLIMIT = [ mysum//i for i in nums ]
visited = []
Solutions = []
Num_Sols = 0
Num_visited = 1

def neb(L):
    global UPLIMIT
    n = len(L)
    ans = []
    for i in range(n):
        L1 = L.copy()
        if L1[i] < UPLIMIT[i]:
            L1[i] += 1
            ans.append(L1)
    return ans


def BFS_combi(n, nums, sum):
    global Solutions, mysum, visited, Num_Sols, Num_visited

    c = [0]*len(nums) # c = [0,0,0]
    Queue = [c]
    visited.append(c)
    while (len(Queue) > 0):
        c = Queue.pop(0)
        for neighbour in neb(c):
            if neighbour not in visited:
                # Queue.append( neighbour )
                visited.append( neighbour )
                Num_visited += 1

                if np.dot(neighbour, nums) == mysum:
                    Num_Sols += 1
                    print("Found combination: ", neighbour, " number of sols found: ", Num_Sols, " Nodes visited: ", Num_visited)
                    Solutions.append(neighbour)
                elif np.dot(neighbour, nums) < mysum:
                    Queue.append( neighbour )
                    

BFS_combi(len(nums), nums, sum)
print( "Total solutions found : ", len(Solutions) )
print( "Total nodes visited : ", len(visited))
