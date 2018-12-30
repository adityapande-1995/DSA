#!python3
# Coin change problem

def change(S,N):
    if N == 0:
        return 1
    if N < 0 or len(S) == 0:
        return 0
    
    include = change( S,N-S[-1] )
    exclude = change( S[:-1],N )
    return include + exclude

# Main
S = [1,2,3,4,5]
N = 20
print("Number of ways to generate change: ",change(S,N))
