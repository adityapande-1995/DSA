#!python3
# Lexicographic ordering example
from math import factorial
from numpy import arange

a = [0,1,2,3]
print("Original", a)

while True:
    # Step 1
    largestI = -1
    for i in arange(0,len(a)-1):
        if a[i] < a[i+1]: largestI = i

    if largestI == -1 : break
	
    # Step 2
    largestJ = -1
    for j in range(len(a)):
        if a[largestI] < a[j]: largestJ = j
	
    # Step 3	
    a[largestI] , a[largestJ] = a[largestJ] , a[largestI]
	
    # Step 4
    a = a[:i+1] + a[i+1:][::-1]	
	
    print("largestI, largestJ", largestI, largestJ, a)
