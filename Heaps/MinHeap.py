#!python3
# Implementing a heap in python
import sys

class MinHeap: # Min heap implementation
    def __init__(self):
        self.A = []
    
    def PARENT(self,i):
        return int((i-1)/2)
    
    def LEFT(self,i):
        return int(2*i + 1)
    
    def RIGHT(self,i):
        return int(2*i + 2)
    
    def size(self):
        return len(self.A)
    
    def empty(self):
        return self.size() == 0

    def heapify_down(self,i):
        left = self.LEFT(i)
        right = self.RIGHT(i)
        smallest = i

        # Compare A[i] with left and right and find smallest value
        if left < self.size() and self.A[left] < self.A[i]:
            smallest = left
        if right < self.size() and self.A[right] < self.A[smallest]:
            smallest = right

        # Swap with child with lesser value and call heapify down recursively
        if smallest != i:
            self.A[i], self.A[smallest] = self.A[smallest], self.A[i]  
            self.heapify_down(smallest)

    def heapify_up(self,i):
        # Check if node at i and its parent violates heap property
        if i and self.A[self.PARENT(i)] > self.A[i]:
            self.A[i], self.A[self.PARENT(i)] = self.A[self.PARENT(i)], self.A[i] 
            self.heapify_up( self.PARENT(i) )

    def push(self, key):
        self.A.append(key)
        index = self.size() - 1
        self.heapify_up(index)

    def pop(self): # Remove element with lowest priority
        try:
            if self.size() == 0:
                print("Heap already empty !")
                sys.exit(0)
            
            # Replace root of heap with last element
            self.A[0] = self.A[-1]
            self.A.pop(-1)
            self.heapify_down(0)
        except:
            print("Random error happened")
    
    def top(self): # Return element with lowest priority
        try:
            if self.size() == 0:
                print("Heap already empty !")
                sys.exit(0)
            else:
                return self.A[0]
            
        except:
            print("Random error happened")


# Main
pq = MinHeap()
pq.push(3)
pq.push(2)
pq.push(15)

print("Size: ",pq.size())
print(pq.top())
pq.pop()
print(pq.top())
pq.pop()

pq.push(5)
pq.push(4)
pq.push(45)
print("Size: ",pq.size())
print(pq.top())
pq.pop()
print(pq.top())
pq.pop()
