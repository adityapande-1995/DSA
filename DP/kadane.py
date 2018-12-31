#!python3
# Kadane's algorithm

def KD(A):
    max_so_far = 0 # Max subarray sum found so far
    max_ending_here = 0 # Max sum of subarrays ending at current position
    for i in range(0,len(A)):
        max_ending_here = max_ending_here + A[i]
        max_ending_here = max(max_ending_here, 0)
        max_so_far = max(max_so_far, max_ending_here)
        print("i : ", i," meh : ", max_ending_here, " msf : ", max_so_far)

    return max_so_far

# Main
a = [1,-5,2]
print("Max subarray sum : ", KD(a))
