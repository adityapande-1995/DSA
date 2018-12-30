#!python3
# Knapsack problem

def KP(v,w,W):
    if W < 0: # Invalid move
        return -100000000
    
    # Base case : trivial
    if len(v) == 0 or W == 0: 
        return 0
    
    include = v[-1] + KP(v[:-1], w[:-1], W-w[-1] )
    exclude = KP(v[:-1], w[:-1], W )

    return max(include,exclude)

# Main
v = [20, 5, 10, 40, 15, 25 ]
w = [  1, 2,  3,  8,  7, 4 ]
W = 10
print("Max knapsack value : ", KP(v,w,W))
