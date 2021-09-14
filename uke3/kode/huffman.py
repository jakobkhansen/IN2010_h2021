from typing import Optional
from heap import PriorityQueue

class Node:
    def __init__(self, frequency, char=None, left=None, right=None) -> None:
        self.frequency = frequency
        self.char = char
        self.left = left
        self.right = right
        self.encoding : Optional[str] = None

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __repr__(self) -> str:
        return f"{self.char} {self.frequency} {self.encoding}"

def build_nodes(input_string : str) -> list[Node]:
    frequencies = {}
    nodes = []

    for char in input_string:
        frequencies[char] = frequencies.get(char, 0) + 1

    for char in frequencies.keys():
        nodes.append(Node(frequencies[char], char))

    return nodes


def build_huffman_tree(nodes : list[Node]) -> Node:
    pq = PriorityQueue()

    for node in nodes:
        pq.insert(node)

    while pq.size() > 1:
        smallest1 = pq.pop()
        smallest2 = pq.pop()

        new_node = Node(smallest1.frequency + smallest2.frequency, left=smallest1, right=smallest2)
        pq.insert(new_node)

    root = pq.pop()


    build_encodings(root)

    return root


def build_encodings(node, path=""):
    node.encoding = path
    if node.char == None:
        build_encodings(node.left, path + '0')
        build_encodings(node.right, path + '1')


def get_encodings(node, encodings=None):
    if encodings == None:
        encodings = {}

    if node.char != None:
        encodings[node.char] = node.encoding
    else:
        get_encodings(node.left, encodings)
        get_encodings(node.right, encodings)

    return encodings


def encode_string(input_string : str, encodings : dict[str, str]) -> str:
    output = ""
    for char in input_string:
        output += encodings[char]

    return output

def decode_string(bit_string : str, huffman_root) -> str:
    output = ""

    i = 0
    while i < len(bit_string):
        current = huffman_root

        while current.char == None:
            bit = bit_string[i]
            if bit == '0':
                current = current.left
                i += 1
            elif bit == '1':
                current = current.right
                i += 1
        output += current.char


    return output


# def main():
sentence = "hello hello goodbye"

print(f"Unencoded: {sentence}")

nodes = build_nodes(sentence)

huffman_root = build_huffman_tree(nodes)

encodings = get_encodings(huffman_root)
print('\n'.join([f"{x}: {y}" for x,y in encodings.items()]))

encoded = encode_string(sentence, encodings)

print(f"Encoded: {encoded}")

decoded = decode_string(encoded, huffman_root)

print(f"Decoded: {decoded}")

# if __name__ == "__main__":
    # main()
