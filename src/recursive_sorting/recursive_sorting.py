def partition(numbers):
    left = []
    pivot = numbers[0]
    right = []

    for val in numbers[1:]:
        if val <= pivot:
            left.append(val)
        else:
            right.append(val)

    return left, pivot, right

def quick_sort(numbers):
    # base case
    if len(numbers) <= 1:
        return numbers

    # figure out how to split
    left, pivot, right = partition(numbers)

    # recursive case
    sorted_array = quick_sort(left) + [pivot] + quick_sort(right)
    return sorted_array

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr

print(merge_sort([2, 1, 3]))

# Understand
# grab a list and split it in half if > 1
# grab two lists and compare them, take the smaller one into a seperate list,
# Repeat untill one list is empty, then add the last item to the new list
# keep grabbing 2 lists untill you've reassembled the data set

# Plan
# Execute
# Review

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
