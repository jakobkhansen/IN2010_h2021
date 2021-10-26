# Dette er et skall man kan bruke for å implementere sorteringsalgoritmer

from random import randint
from collections import deque


NUM_TESTS = 3
MAX_ELEM = 100
MAX_ARRAY_SIZE = 1000000

# Tar inn et array, burde returnere et sortert array med samme elementer
# Kan være samme array som input

# Dette er en veldig forenklet versjon av Timsort
def sort(array: list[int]):

    if len(array) < 64:
        insertion_sort(array, 0, 0, len(array))
        return array

    minrun = 32

    runs = find_runs(array, minrun)
    
    merge_runs(array, runs)

    return array



# Inserts elementer inn i [l, start] fra [start, r]. Ender opp med at [l, r] er sortert
# Ikke inclusive r, inclusive l
def insertion_sort(array, start : int, l : int, r : int):
    for i in range(start, min(r+1, len(array)+1)):
        j = i-1
        while j >= l+1 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1


def find_runs(array, minrun):
    runs = []
    i = 0
    while i < len(array):

        if i >= len(array)-1:
            runs.append((i,i+1))
            break

        decreasing = False


        if array[i] < array[i+1]:
            decreasing = True

        j = i

        if decreasing:
            while j < len(array)-1 and array[j+1] < array[j]:
                j += 1
            j = j-1
            invert_decreasing_run(array, i, j)
        else:
            while j < len(array)-1 and array[j+1] >= array[j]:
                j += 1
            j = j-1

        runsize = abs(j-i)
        
        if runsize < minrun:
            insertion_sort(array, j, i, i+minrun)
            runsize = minrun

        runs.append((i, min(len(array), i+runsize)))
        i += runsize
    return runs

def invert_decreasing_run(array, l, r):
    while l < r:
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1

def merge_runs(array : list[int], runs : list[tuple[int, int]]):
    while len(runs) > 1:
        new_runs = []
        while len(runs) > 0:
            if len(runs) == 1:
                new_runs.append(runs.pop())
                continue
            # Pop two runs to be merged
            l1,r1 = runs.pop()
            l2,r2 = runs.pop()

            (l1, r1), (l2, r2) = sorted([(l1,r1), (l2,r2)], key=lambda x: x[0])

            start = l1

            merged = []

            while l1 < r1 and l2 < r2:
                if array[l1] <= array[l2]:
                    merged.append(array[l1])
                    l1 += 1
                else:
                    merged.append(array[l2])
                    l2 += 1

            while l1 < r1:
                merged.append(array[l1])
                l1 += 1

            while l2 < r2:
                merged.append(array[l2])
                l2 += 1


            for i in range(len(merged)):
                array[start+i] = merged[i]        

            new_runs.append((start, start+len(merged)))

        runs = new_runs

def run_test():
    num_passed = 0
    for i in range(NUM_TESTS):
        array = [int(randint(0, MAX_ELEM)) for x in range(MAX_ARRAY_SIZE)]

        unsorted_copy = array.copy()
        sorted_copy = sorted(array.copy())

        result = sort(array)

        if result != sorted_copy:
            print(f"FAILED TEST #{i}")
            print(f"ORIGINAL: {str(unsorted_copy)}")
            print(f"SORTED: {str(result)}")
            print()
        else:
            num_passed += 1

    print(f'{num_passed} of {NUM_TESTS} tests passed')

def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True

if __name__ == "__main__":
    run_test()
