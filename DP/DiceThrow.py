#!python3
# n dice with 1 to k faces. Find number of ways to produce a given sum.

def dice(n,k,s):
    # No. of dice finished (Base case)
    if n == 0:
        return s == 0
    # Impossible states
    if s < 0 or k*n < s or n > s:
        return 0
    
    return sum( [dice(n-1, k, s-i) for i in range(1,k+1)] )

# Main
n = 4
k = 6
s = 15
print("Total no of ways : ", dice(n,k,s))
