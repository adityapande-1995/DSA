#!python3
# Knights' walk attempt using BFS
import sys

def is_inside_board(pos, n):
    return pos[0] >=1 and pos[0] <= n and pos[1] >= 1 and pos[1] <= n

def valid_neighbours(B,n):
    attempt_moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1), (-1,-2),(1,-2),(2,-1)]
    neighbours = []
    for i in range(8):
        board_pos = (B[-1][0] + attempt_moves[i][0], B[-1][1] + attempt_moves[i][1] )
        if board_pos not in B and is_inside_board(board_pos, n):
            new_board = B.copy()
            new_board.append(board_pos)
            neighbours.append(new_board)
    
    return neighbours

def walk_BFS(B,n):
    Queue = [B]
    visited = [B]
    print("Starting walk from given board ",B)
    while len(Queue) != 0:
        v = Queue.pop(0)
        for neb in valid_neighbours(v.copy(), n): # All valied neighbours
            if neb not in visited:
                Queue.append(neb)
                visited.append(neb)
                if len(visited)%100 : print("Total states visited : ",len(visited))
                # print("Visited state ",neb)
                if len(neb) == n*n :
                    print("Found solution: ",neb)
                    print("Totoal nodes visited: ",len(visited))

dfs_vis = 0
def walk_DFS(B,n):
    global dfs_vis
    # print("Visited game with moves : ",len(B) )#, B)
    if dfs_vis%10**5 == 0: print("Total states visited : ",dfs_vis)
    # Found solution
    if len(B) == n*n :
        print("Found solution: ",B)
        print("Total nodes visited: ",dfs_vis)
        sys.exit(0)
    # Else
    dfs_vis += 1
    for neb in valid_neighbours(B.copy(), n):
        walk_DFS(neb, n)


# Main
Board = [(1,1)] # Knight at bottom left corner of board
board_size = 8 
# walk_BFS(Board,board_size) 
walk_DFS(Board,board_size) # Took me 8250732 nodes to get 1st result




