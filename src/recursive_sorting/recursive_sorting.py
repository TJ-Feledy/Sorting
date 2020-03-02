# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    # TO-DO
    index,left,right = 0,0,0

    while left < len(arrA) and right < len(arrB):
        if arrA[left] < arrB[right]:
            merged_arr[index] = arrA[left]
            left = left + 1
        else:
            merged_arr[index] = arrB[right]
            right = right + 1
        index = index + 1

    while left < len(arrA):
        merged_arr[index] = arrA[left]
        left = left + 1
        index = index + 1

    while right < len(arrB):
        merged_arr[index] = arrB[right]
        right = right + 1
        index = index + 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)
        merge(left,right)

    return arr

print(merge_sort([5,6,2,1,3,7,4]))
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
