from heap import PriorityQueue

class Node:
    def __init__(self) -> None:
        pass


def build_nodes(input_string : str) -> list[Node]:
    pass

def build_huffman_tree(nodes : list[Node]) -> Node:
    pass


def build_encodings(nodes : list[Node]) -> dict[str, str]:
    pass



def encode_string(input_string : str, encodings : dict[str, str]) -> str:
    pass

def decode_string(input_string : str, huffman_root : Node) -> str:
    pass




def main():
    sentence = "det er veldig vanskelig aa finne paa en lang eksempelsetning"

    nodes = build_nodes(sentence)

    huffman_root = build_huffman_tree(nodes)

if __name__ == "__main__":
    main()
