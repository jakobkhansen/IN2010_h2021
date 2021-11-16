import sys

def ultraquicksort():
    n = int(input())
    # nums = [int(input()) for x in range(n)]
    nums = [x for x in range(13, 0, -1)]

    return merge_sort(nums, 0, len(nums) - 1)


def merge_sort(nums, low, high):
    counter = 0
    if (low >= high):
        return 0

    mid = low + (high - low) // 2

    counter += merge_sort(nums, low, mid)
    counter += merge_sort(nums, mid+1, high)

    counter += merge(nums, low, mid, high)

    return counter

def merge(nums, low, middle, high):

    counter = 0
    left = nums[low:middle+1]
    right = nums[middle+1:high+1]


    leftIndex = 0
    rightIndex = 0
    arrayIndex = low

    while (leftIndex < len(left) and rightIndex < len(right)):
        if left[leftIndex] <= right[rightIndex]:
            nums[arrayIndex] = left[leftIndex]
            leftIndex += 1
        else:
            nums[arrayIndex] = right[rightIndex]
            rightIndex += 1
            counter += len(left) - leftIndex

        arrayIndex += 1

    while (leftIndex < len(left)):
        nums[arrayIndex] = left[leftIndex];
        leftIndex += 1
        arrayIndex += 1

    while rightIndex < len(right):
        nums[arrayIndex] = right[rightIndex];
        rightIndex += 1
        arrayIndex += 1

    return counter






def main():
    print(ultraquicksort())
main()
