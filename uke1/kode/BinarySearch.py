import bisect

def binary_search(array : list[int], elem : int):
    low = 0
    high = len(array)

    while low < high:
        middle = (low + high) // 2

        if array[middle] == elem:
            return middle
        elif array[middle] > elem:
            high = middle - 1
        elif array[middle] < elem:
            low = middle + 1

    return -1

a = [1,2,3,5,7,8,10,20,40]
print(binary_search(a, 7))
