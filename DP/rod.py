#!python3
# Rod length cutting problem

def rodcut(price, rod_len):
    if rod_len == 0:
        return 0
    else:
        return max( [ price[i-1]+rodcut(price,rod_len-i) for i in range(1,rod_len+1)] )

# Main
length = [1,2,3,4,5,6,7,8]
price = [1, 5, 8, 9, 10, 17, 17, 20]
n = 4
print("Max value : ",rodcut(price,n))
