import bisect

def binary_search(array : list[int], elem : int):
    low = 0
    high = len(array)-1

    while low <= high:
        middle = (low + high) // 2

        if array[middle] == elem:
            return middle
        elif array[middle] > elem:
            high = middle - 1
        elif array[middle] < elem:
            low = middle + 1

    return -1
