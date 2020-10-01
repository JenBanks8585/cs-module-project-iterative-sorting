#def linear_search(arr, target):
#    # Your code here
#
#
#    return -1   # not found
#
#
## Write an iterative implementation of Binary Search
#def binary_search(arr, target):
#
#    # Your code here
#
#
#    return -1  # not found
#
data = [2, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 17, 21, 23, 24, 25, 28, 29, 30, 32]
target = 10

import time

start_time = time.time()
#Linear Search
def linear_search(data,target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

print(linear_search(data, target))

end_time = time.time()
print (f"runtime: {end_time - start_time} seconds")


start_time1 = time.time()
#Iterative Binary Search
def binary_search(data, target):
    low = 0
    high = len(data)-1

    while low <= high:
        mid = (low + high)//2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(binary_search(data,target))
end_time1 = time.time()
print (f"runtime: {end_time1 - start_time1} seconds")


start_time2 = time.time()
#recursive Binary search
def bin_searc_recur(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return bin_searc_recur(data, target, low, mid-1)
        else:
            return bin_searc_recur(data, target, mid + 1, high)
    return 'Sorry that number is not in the list'

print(bin_searc_recur(data, target, 2, 32))
end_time2 = time.time()
print (f"runtime: {end_time2 - start_time2} seconds")
