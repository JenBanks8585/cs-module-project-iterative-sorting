# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        #cur_index = i
        smallest_index = i #cur_index

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        if smallest_index != i:
            arr[smallest_index], arr[i]= arr[i], arr[smallest_index]
        
    return arr

        
print(selection_sort([2,4,3,5,6,7,1,1,2,4,9,8]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    sorted = False  # variable to use to break out of the while loop

    while not sorted:
        sorted = True    # when sorted, break the loop

        for i in range(0, len(arr)- 1):
            if arr[i] > arr[i + 1]:       # if prev is greater than next
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1] , arr[i]   # switch order

    return arr

print(bubble_sort([2,4,3,5,6,7,1,1,2,4,9,8]))
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr):
    maximum=max(arr)

    num_counter = [0 for i in range(maximum + 1)]
    sorted_list = []
    for i in arr:
      num_counter[i] +=1

    for i in range(len(num_counter)):
      if num_counter[i] != 0:
        sorted_list +=[i for n in range(num_counter[i])]


    return sorted_list

arr1 = [3, 4, 7, 1, 8, 9, 12, 3, 4, 5, 7]

print(counting_sort(arr1))