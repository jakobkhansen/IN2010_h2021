# Avgjør hvilken O-notasjon hver funksjon er i

# 1. n er len(array)
def sum_three_elements(array : list[int]) -> int:
    return array[0] + array[1] + array[2]

# 2. n er len(input_string)
def string_contains_space(input_string : str) -> bool:
    for char in input_string:
        if char == ' ':
            return True
    return False

def print_number_many_times(n : int) -> None:
    for _ in range(20):
        print(n)

# 3. n er len(array)
def contains_duplicate(array : list[int]) -> bool:
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] == array[j]:
                return True
    return False


# 4. n er len(array)
def contains_duplicate_smarter(array : list[int]) -> bool:
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                return True
    return False

# 5. n er n :)
def multiply_by_two(n : int) -> None:
    current = 1
    while current <= n:
        print(current)
        current = current * 2



# 6. n er len(array1), m = len(array2)
def sums_multiplied(array1 : list[int], array2 : list[int]) -> int:
    sum1 = 0
    sum2 = 0

    for element in array1:
        sum1 += element

    for element in array2:
        sum2 += element

    return sum1*sum2


# 7. n er len(array1), m er len(array2), k er k :)
def sums_multiplied_k_times(array1 : list[int], array2 : list[int], k : int):
    sum = 0
    for _ in range(k):
        sum += sums_multiplied(array1, array2)

# Ekstra: n er len(array)
# Se her: https://wiki.python.org/moin/TimeComplexity
def get_array_sorted(array : list[int]) -> list[int]:
    return sorted(array)
