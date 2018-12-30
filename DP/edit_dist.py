#!python3
# Edit distance problem : transform X to Y

def ED(X,Y):
    m,n = len(X), len(Y)

    # Case 1 : one string becomes empty
    if m == 0:
        return n
    if n == 0:
        return m
    
    # Case 2 : Last character matches
    if X[-1] == Y[-1]:
        return 0 + ED( X[:-1], Y[:-1] )
    else: # Case 3
        a = 1 + ED( X, Y[:-1]) # Insert last char of Y in X
        b = 1 + ED( X[:-1], Y) # Delete last char of X
        c = 1 + ED( X[:-1], Y[:-1]) # Substitute last of X by last of Y
        return min(a,b,c)

# Main
print("Edit distance is : ", ED("kitten","sitting"))
