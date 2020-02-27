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

print(insertion_sort([5, 6, 1, 9, 7, 2, 3]))

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr