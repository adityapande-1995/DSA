#!python3
# Subset sum problem

def SS(L,s):
    # Base cases
    if s == 0:
        return True
    if len(L) == 0 and s != 0:
        return False

    # Recursion
    if L[-1] > s :
        return SS(L[:-1], s)
    else:
        return SS(L[:-1], s) or SS(L[:-1], s-L[-1])

# Main
print(SS([3, 34, 4, 12, 5, 2], 35))
