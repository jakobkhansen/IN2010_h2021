import sys

def weakvertices(lines):
    index = 0
    while int(lines[index]) != -1:
        size = int(lines[index])
        matrix = [[int(x) for x in y.split(" ")] for y in lines[index+1:index+size+1]]

        # Skriv løsning her, bruk matrix!
        print(matrix)

        index += size+1
                

def neighbours(matrix, i, j):
    return matrix[i][j] == 1

def main():
    lines = [line.strip() for line in sys.stdin]
    weakvertices(lines)
main()

