#!python3

a = [4,3,2,1]
b = []
c = []

def T(n, B, A, E):
    global a,b,c
    print("Current status : ", a, b, c)
    if n == 1:
        E.append( B.pop() )
        return
    
    T(n-1, B, E, A)
    T(1, B, A, E)
    T(n-1, A, B, E)

T(len(a), a, b, c)
print("Final solution: ",a,b,c)