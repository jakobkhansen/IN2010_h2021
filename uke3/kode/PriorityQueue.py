from random import randint, random


def parent(index):
    return (index-1) // 2

def left_child(index):
    return index*2 + 1

def right_child(index):
    return index*2 + 2


class PriorityQueue:
    def __init__(self) -> None:
        self.array = []

    def insert(self, element):
        index_inserted = len(self.array)
        self.array.append(element)
        self.bubbleUp(index_inserted)


    def pop(self):

        if len(self.array) == 1:
            return self.array.pop()

        smallest = self.array[0]

        self.array[0] = self.array.pop()

        self.bubbleDown(0)

        return smallest

    def bubbleUp(self, index):
        if index == 0:
            return

        if self.array[index] < self.array[parent(index)]:
            self.swap(index, parent(index))
            self.bubbleUp(parent(index))


    def bubbleDown(self, index):
        n = len(self.array)

        if right_child(index) < n:
            left_value = self.array[left_child(index)]
            right_value = self.array[right_child(index)]

            smallestChild = left_child(index) if left_value < right_value else right_child(index)

            if self.array[smallestChild] <= self.array[index]:
                self.swap(index, smallestChild)
                self.bubbleDown(smallestChild)

        elif left_child(index) < n and self.array[left_child(index)] <= self.array[index]:
            self.swap(index, left_child(index))

    def swap(self, index1, index2):
        self.array[index1], self.array[index2] = self.array[index2], self.array[index1]

def test():
    queue = PriorityQueue()


    for _ in range(10000, 0, -1):
        queue.insert(randint(0, 1000000))

    last = queue.pop()
    print(queue.pop())
    for _ in range(len(queue.array), 0, -1):
        smallest = queue.pop()
        print(smallest)
        assert smallest >= last
        last = smallest


test()
