# TO-DO: complete the helper function below to merge 2 sorted arrays

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    
    # Your code here
    # 2 sorted arrays are passed in
    # must return one sorted array
    # initialize a pointer to store the first element of the array
    # also initialize a pointer for the sorted array
    # then increment the pointer by 1 after adding a value to the c array
    a = 0
    b = 0
    for i in range(len(merged_arr)):
        if arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] >= arrB[b]:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr
merge([2,3], [6,7])
# TO-DO: implement the Merge Sort function below recursively
# Breaks array down to single elements and builds back up while sorting
def merge_sort(arr):
    # Your code here
    
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[0:middle]
        right = arr[middle:]
        left_merge = merge_sort(left)
        right_merge = merge_sort(right)
        merge(left_merge, right_merge)
        



        


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

