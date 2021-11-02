# type: ignore
import string
import random
from collections import deque

# Hashmap implemented using open addressing
# Collisions are handled with linear probing


class HashMap:
    def __init__(self) -> None:
        self.array = [None]
        self.num_elems = 0
        self.load_factor = 0.75

    # Get value from key
    def __getitem__(self, key):
        return self.find(key)


    # Insert / replace key
    def __setitem__(self, key, value) -> None:
        self.insert(key,value)


    # Allows us to use len(hashmap), gives number of elements in map
    def __len__(self):
        return self.num_elems

    # Resizes the table if necessary
    def dynamic_resize(self):
        if (self.num_elems / len(self.array)) >= self.load_factor:
            self.table_double()

    def __iter__(self):
        for bucket in self.array:
            if bucket:
                for kv in bucket:
                    yield kv

    # Doubles size of table and inserts elements in new table
    def table_double(self) -> None:
        old_vals = [(key,val) for key,val in self]

        self.array = [None]*(len(self.array)*2)

        self.num_elems = 0

        for key,val in old_vals:
            self.insert(key,val)


    # Gets the index where a key wants to be placed
    def get_hash_index(self, key) -> int:
        return hash(key) % len(self.array)

    def insert(self, key, val):
        hash_index = self.get_hash_index(key)
        list_at_hash = self.array[hash_index] if self.array[hash_index] != None else deque()
        for i,(iter_key,iter_value) in enumerate(list_at_hash):
            if iter_key == key:
                list_at_hash[i] = (key,val)
                return

        list_at_hash.append((key,val))
        self.array[hash_index] = list_at_hash
        self.num_elems += 1
        self.dynamic_resize()

    def find(self, key):
        hash_index = self.get_hash_index(key)
        list_at_hash = self.array[hash_index] if self.array[hash_index] != None else deque()
        for (iter_key,value) in list_at_hash:
            if iter_key == key:
                return (value)
        return None

    def delete(self, key):
        hash_index = self.get_hash_index(key)
        list_at_hash = self.array[hash_index] if self.array[hash_index] != None else deque()
        for i,(iter_key,value) in enumerate(list_at_hash):
            if iter_key == key:
                del list_at_hash[i]
                return

    def __repr__(self) -> str:
        return str(self.array)

    def __str__(self) -> str:
        return self.__repr__()




# type: ignore
def test():
    INSERT_ITEMS = 10000
    DELETE_ITEMS = INSERT_ITEMS // 10
    low_alpha = string.ascii_lowercase
    randint = random.randint

    print('GENERATING INPUTS')
    insert_strings = list(set([
        (''.join([random.choice(low_alpha) for _ in range(randint(1,10))]))
    for _ in range(INSERT_ITEMS)]))


    insert_pairs = [(x, random.randint(0,1000)) for x in insert_strings]


    hashmap = HashMap()

    # Insert elements
    print(f"INSERTING {INSERT_ITEMS} elements")
    for key,val in insert_pairs:
        hashmap[key] = val

    # print('\nHASHMAP RESULT')
    # print(hashmap.array, '\n')

    # Assert len
    assert len(hashmap) == len(insert_pairs)

    # Assert insertions
    for key,val in insert_pairs:
        assert hashmap[key] == val

    # Delete some of them
    # print(f'DELETING {DELETE_ITEMS} elements\n')
    for key,val in insert_pairs[:DELETE_ITEMS]:
        hashmap.delete(key)

    # Assert deleted
    for key,val in insert_pairs[:DELETE_ITEMS]:
        assert hashmap[key] == None

    

    # Assert insertions still working
    print(f'RETESTING insertions')
    for key, val in insert_pairs[DELETE_ITEMS:]:
        assert hashmap[key] == val

    # print('\nHASHMAP RESULT')
    # print(hashmap, '\n')


    print('\nTEST SUCCESSFUL')

if __name__ == "__main__":
    test()
