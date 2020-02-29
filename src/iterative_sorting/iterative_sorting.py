def insertion_sort(arr):

    #loop over all the numbers starting at index 1
    for i in range(1, len(arr)):
        # save each number into a temporary variable
        current_num = arr[i]
        
        j = i
        # loop until we reach the end of array or the number we are comparing is not smaller than its neighbor
        while j > 0 and current_num < arr[j - 1]:
            # move the left number over to the right 1 spot
            arr[j] = arr[j-1]        
            j -= 1
        # save the temporary number in its correct spot
        arr[j] = current_num

    return arr

# TO-DO: Complete the selection_sort() function below 

# Understand
# - get number at index 0
# - check if the number is greater
#   than the one to it's left until
#   it finds one unless the list ends
# - when it finds one, replace places with the number
# - continue the check with the next index ++

# Plan
# Start with current index = 0
# For all indices EXCEPT the last index:

# a. Loop through elements on right-hand-side
# of current index and find the smallest element

# b. Swap the element at current index with the
# smallest element found in above loop

# Execute

# Review

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

# print(selection_sort([5, 6, 1, 9, 7, 2, 3]))

# TO-DO:  implement the Bubble Sort function below

# Loop through the entire array and compare the current value
# to the value to the right of it
# If the current value is larger than the one to the right, swap them
# Keep doing this until a swap does not happen.

def bubble_sort( arr ):
    swapped = True
    # while swap happened
        # loop through the array and compare values
        # if value at current index is bigger than value at index to the right.
            # swap them
            # The largest value should end up at the end
            # once that value is at the end then you just start the while over 
            # keep doing this until a swap doesn't happen
    while swapped:
        swapped = False
        for j in range(0, len(arr)-1):
            if arr[j]>arr[j+1]:
                # Do swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            
    return arr

print(bubble_sort([6, 2, 8, 4]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr