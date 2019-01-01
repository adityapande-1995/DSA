#!python3
# Matrix chain multiplication problem

def Mat(L):
    if len(L) == 3:
        return L[0]*L[1]*L[2]
    else:
        options = []
        for i in range(1, len(L)-1):
            cost1 = L[i-1]*L[i]*L[i+1]
            b = L.copy() ; b.pop(i)
            cost2 = Mat(b)
            options.append(cost1 + cost2)
        
        return min(options)

a = [40, 20, 30, 10, 30] # Matrices are (40,20), (20,30), (30,10) ... in size
print("Min cost of multiplication", a, " is ", Mat(a))
