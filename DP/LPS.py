#!python3
# Longest palindromic subsequence

def LPS_len(X,i,j):
    # Base cases
    if i > j:
        return 0
    if i == j:
        return 1
    
    # If first and last letter is same
    if X[i] == X[j]:
        return LPS_len(X, i+1, j-1) + 2
    else: # If not same
        return max( LPS_len(X, i+1, j), LPS_len(X, i, j-1))

# Main
X = "xyzzyspoon"
print( "Longst palindrome subsequence length :", LPS_len(X,0,len(X)-1) )

