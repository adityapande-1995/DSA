#!python3
# Travelling salesman problem 
import random

n = 3 # No of points
points = [(random.uniform(0,10), random.uniform(0,10)) for i in range(n)]

def cost(i,j):
    global points
    return (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2

def minPathCost(i,s):
    # Base case
    if len(s) == 0:
        return cost(i,0)
    else:
        options = []
        for k in s:
            scopy = s.copy() ; scopy.remove(k)
            options.append( cost(i,k) + minPathCost(k , scopy)  )

        return min(options)

if __name__ == '__main__':
    print("Your points are ", points)
    print("Min length of path is: ", minPathCost(0,list(range(n))))


