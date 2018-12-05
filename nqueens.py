#!python3
import numpy as np
from itertools import permutations

def diag_attack(m):
    r,c = m.shape
    q = np.flip(m,0)
    flag = False
    for i in np.arange(-c,c+1):
        if m.trace(offset=i) > 1 or q.trace(offset=i) > 1:
            flag = True
            break
    
    return flag

# Main
# For n rooks problem
N = 8
l = list(permutations([i for i in range(N)]))
solutions = []
print("Total ", len(l), " solutions for n rook problem")
b = np.eye(N,N)
b1 = b.copy()

for combi in l:
    for i in range(N):
        b[:,i] = b1[:,combi[i]]
    solutions.append(b.copy())

# Printing N rook answers
# for s in solutions:
#     print("")
#     print(s)

# For n queens problem
print("****** Running n queens ******")
solutions1 = []
for s in solutions:
    if not diag_attack(s):
        solutions1.append(s)
        # Printing N queen answers
        # print("")
        # print(s)

print("Found ",len(solutions), " answers to n rooks and ", len(solutions1), " to n queens")
print(solutions1[0])


