import sys

def weakvertices(lines):
    index = 0
    while int(lines[index]) != -1:
        weak = []
        size = int(lines[index])
        matrix = [[int(x) for x in y.split(" ")] for y in lines[index+1:index+size+1]]
        index += size+1
        # print(matrix)
        for i in range(len(matrix)):
            is_weak = True
            for j in range(len(matrix)):
                for k in range(len(matrix)):
                    if neighbours(matrix, i, j) and neighbours(matrix, i, k) and neighbours(matrix, j, k):
                        is_weak = False
                        break
                if not is_weak:
                    break
            if is_weak:
                weak.append(i)
        print(" ".join([str(x) for x in weak]))
                

def neighbours(matrix, i, j):
    return matrix[i][j] == 1

def main():
    lines = [line.strip() for line in sys.stdin]
    weakvertices(lines)
main()
