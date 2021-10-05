
print("String permutations")
def string_permutations(string1, string2):
    letter_counts = {}

    for letter in string1:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    for letter in string2:
        letter_counts[letter] = letter_counts.get(letter, 0) - 1

    for key,value in letter_counts.items():
        if value != 0:
            return False

    return True

inputs = [
    ['test', 'tset'],
    ['algorithm', 'logarithm'],
    ['data', 'dat'],
    ['something', ''],
    ['', '']
]

for input in inputs:
    print(f"Testing input: {input} => {string_permutations(*input)}")
print()


print('Document search')
def document_search_wordcount(document, keyword):
    # Cheating solution => return document.split().count(keyword)
    keyword_count = 0

    for i in range(len(document)-len(keyword)):
        is_keyword = True
        for j in range(i, i+len(keyword)):
            if document[j] != keyword[j-i]:
                is_keyword = False
        if is_keyword:
            keyword_count += 1


    return keyword_count


inputs = [
    ['This is a very very long document', 'very'],
    ['Hello World Goodbye World', 'Hello'],
    ['Not a long document', 'very']
]

for input in inputs:
    print(f"Testing input: {input} => {document_search_wordcount(*input)}")
print()


print('Cache document')
def cache_document_word_count(document):
    cache = {}
    for word in document.split():
        cache[word] = cache.get(word, 0) + 1

    return cache

for input in inputs:
    cache = cache_document_word_count(input[0])
    print(f"Testing input: {input} => {cache.get(input[1], 0)}")
print()


print('Build longest string')
def build_longest_string(a, b, c):
    longest = []

    counts = {
        'a':a,
        'b':b,
        'c':c
    }

    prev_count = {
        'a':0,
        'b':0,
        'c':0
    }

    while True:
        available = {key:value for key,value in counts.items() if prev_count[key] < 2 and value > 0}

        if len(available) == 0:
            break

        next_letter = max(available.keys(), key=lambda x : available[x])
        longest.append(next_letter)

        for key in prev_count:
            if key != next_letter:
                prev_count[key] = 0

        prev_count[next_letter] += 1
        counts[next_letter] -= 1

    return ''.join(longest)


inputs = [
    [1,2,3],
    [3,3,3],
    [1,1,99],
    [5,5,0]
]

for input in inputs:
    print(f"Testing input: {input} => {build_longest_string(*input)}")
print()


print('Array zero-sum')
def zero_sum_array(N):
    array = []

    if N % 2 != 0:
        array.append(0)

    i = 1
    while len(array) < N:
        array.append(i)
        array.append(-i)
        i += 1
    return array

inputs = [
    3,
    5,
    1,
    2
]

for input in inputs:
    print(f"Testing input: {input} => {zero_sum_array(input)}")



