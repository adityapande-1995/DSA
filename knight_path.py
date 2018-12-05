#!python3
import sys

N = 5
XL = [1,2,2,1,-1, -2,-2,-1]
YL = [2,1,-1,-2,-2,  -1,1,2]
Start = [0,0]
End = [3,1]

def DFSWalk(current, stack):
    global XL, YL, End, N
    stack.append(current)
    # print("Currently at ",current)
    if current == End:
        print("Reached destination, current stack :", stack)
        sys.exit()
        return 1
    else:
        for i in range(8):
            nextX = current[0] + XL[i]
            nextY = current[1] + YL[i]
            if ( [nextX,nextY] not in stack ) and (nextX >= 0 and nextY >= 0 and nextX < (N) and nextY < (N) ):
                print("Moving to X,Y :", nextX, nextY, " using ", XL[i],YL[i])
                k = DFSWalk( [nextX,nextY], stack )
    
# Main
DFSWalk(Start, [])