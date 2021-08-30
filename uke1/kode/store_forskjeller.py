import random
import time

def slow(array : list[int]):
    sum = 0
    for i in array:
        for j in array:
            sum += i*j
    return sum

def fast(array : list[int]):
    sum = 0
    for i in array:
        sum += i
    return sum


print("Lager array")

array = [random.randint(0, 1000) for _ in range(1000)]
# array = [random.randint(0, 1000) for _ in range(10000000)]

print("Kjører fast:")
t1 = time.time()
fast(array)
t2 = time.time()
print(f"Tid: {t2 - t1}")

print("Kjører slow:")
t1 = time.time()
slow(array)
t2 = time.time()
print(f"Tid: {t2 - t1}")
