
# Dette er et skall man kan bruke for å implementere sorteringsalgoritmer

from random import randint, shuffle


NUM_TESTS = 10
MAX_ELEM = 100
MAX_ARRAY_SIZE = 10

# Tar inn et array, burde returnere et sortert array med samme elementer
# Kan være samme array som input
def sort(array: list[int]):

    # Sorter array her!
    while not is_sorted(array):
        shuffle(array)
    print(array)

    return array


def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True

def run_test():
    num_passed = 0
    for i in range(NUM_TESTS):
        array = [int(randint(0, MAX_ELEM)) for x in range(randint(0,MAX_ARRAY_SIZE))]

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


if __name__ == "__main__":
    run_test()
