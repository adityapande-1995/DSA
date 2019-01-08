#!python3
# Seive of Erathosthenes for numbers less than n

def soe(n):
    prime = [True]*n
    p = 2
    while (p**2 <= n):
        if (prime[p] == True):
            for i in range(p*2, n, p):
                prime[i] = False
        
        p += 1
  
    return [p for p in range(2,n) if prime[p] ]

print(soe(100))
