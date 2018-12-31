#!python3
# fIND KTH LARGEST ELEMENT IN O(nlog(k)) time
import heapq

def k_L(L,k):
    H = L[:k]
    heapq.heapify(H)
    for n in L[k:] :
        if n > H[0]:
            heapq.heappop(H)
            heapq.heappush(H,n)
    
    return heapq.heappop(H)

# Main
a = [7,4,6,3,9,1]
k = 2
print("kth largest element is : ",k_L(a,k))
