def hash_sum(word):
    return sum([ord(c) for c in word])

def hash_better(word):
    sum = 7
    for i,c in enumerate(word):
        sum += ord(c)*(31**i)
    return sum

word = "ehllo"

print(hash_sum(word))
print(hash_better(word))
