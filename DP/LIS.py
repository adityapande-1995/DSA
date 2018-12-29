#!python3
# Longest Increasing subsequence

def LIS_len(x,i,n, prev = -100000):
    if i == n:
        return 0
    
    # When item is excluded from list
    exclu = LIS_len(x, i+1, n, prev) 
    # Item is included
    inclu = 0
    if x[i] > prev:
        inclu = LIS_len(x, i+1, n, x[i]) + 1

    return max(exclu, inclu)


# Main
st = [1,2,3,4,5,0]
print("Array : ", st)
print("LIS length : ", LIS_len(st,0,len(st)) )
