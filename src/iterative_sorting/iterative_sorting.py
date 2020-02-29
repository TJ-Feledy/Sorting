# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # at current check the rest of list for smaller number
        for i2 in range(cur_index + 1, len(arr)):
          if arr[i2] < arr[smallest_index]:
            # set new smallest index
            smallest_index = i2

            



        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
      # at each index check if next index is less then swap
      for i2 in range(0, len(arr)-1-i):
        if arr[i2] > arr[i2+1]:
          arr[i2], arr[i2+1] = arr[i2+1], arr[i2]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr