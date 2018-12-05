#!python3
import sys

N = 8
XL = [1,2,2,1,-1, -2,-2,-1]
YL = [2,1,-1,-2,-2,  -1,1,2]
Start = [0,0]
End = [4,0]

def DFSWalk(current, visited=[]):
    global XL, YL, End, N
    visited.append(current)
    # print("Currently at ",current)
    if current == End:
        print("Reached destination, visited total nodes :", len(visited))
        sys.exit()
        return 1
    else:
        for i in range(8):
            nextX = current[0] + XL[i]
            nextY = current[1] + YL[i]
            if ( [nextX,nextY] not in visited ) and (nextX >= 0 and nextY >= 0 and nextX < (N) and nextY < (N) ):
                print("Moving to X,Y :", nextX, nextY, " using ", XL[i],YL[i])
                k = DFSWalk( [nextX,nextY], visited )

def BFSWalk(current):
    global XL, YL, End, N
    Queue = [] 
    Queue.append(current)
    visited = [current]
    while (len(Queue) > 0):
        v = Queue.pop(0)
        # print("v :",v)
        for i in range(8):
            nextX = v[0] + XL[i] ; nextY = v[1] + YL[i]
            if ( [nextX,nextY] not in visited ) and (nextX >= 0 and nextY >= 0 and nextX < (N) and nextY < (N) ):
                Queue.append( [nextX,nextY] )
                visited.append( [nextX,nextY] )
                print("visited :", [nextX,nextY])
            
                if [nextX,nextY] == End:
                    print("Found target, visited total ", len(visited), " nodes")
                    return


# Main
print("\n*** Starting Breadth First Search ***")
BFSWalk(Start)
print("\n*** Starting Depth First Search ***")
DFSWalk(Start)
