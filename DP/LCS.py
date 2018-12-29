#!python3
# Longest common subsequence

def LCS_len(X,Y): # O( 2**(len(X)+len(Y)) ) Simple code
    # Base case
    m,n = len(X), len(Y)
    if m == 0 or n == 0:
        return 0
    
    # if last character matches
    if X[-1] == Y[-1]:
        return LCS_len(X[:-1], Y[:-1]) + 1
    # if last character doesnt match
    return max(LCS_len(X[:-1],Y), LCS_len(X,Y[:-1]) )

lookup = {}
def LCS_len_memo(X,Y): # O(m*n)  Memoized code
    global lookup
    m,n = len(X), len(Y)
    if m == 0 or n == 0:
        lookup[(m,n)] = 0
    
    if (m,n) not in lookup:
        if X[-1] == Y[-1]:
            lookup[(m,n)] =  LCS_len_memo(X[:-1], Y[:-1]) + 1
        else:
            lookup[(m,n)] = max( LCS_len_memo(X[:-1],Y), LCS_len(X,Y[:-1]) )
        
    return lookup[(m,n)]

def LCS(X,Y): # Uses lookup dictionary
    global lookup
    m,n = len(X), len(Y)
    if m == 0 or n == 0:
        return ""

    if X[-1] == Y[-1]: # if last character is same
        return LCS(X[:-1], Y[:-1]) + X[-1]
    else:
        if lookup[(m-1,n)] > lookup[(m,n-1)] :
            return LCS(X[:-1], Y)
        else:
            return LCS(X, Y[:-1])

# Main
X = "hello1234"
Y = "yellow13"
print("LCS length: ", LCS_len(X,Y), LCS_len_memo(X,Y))

# Need to complete entire lookup table
for i in range(len(X)+1):
    for j in range(len(Y)+1):
        LCS_len_memo(X[:i], Y[:j])

# print(lookup)
print("String: ", LCS(X,Y))
