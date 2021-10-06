# type: ignore
import string
import random

# Hashmap implemented using open addressing
# Collisions are handled with linear probing


class HashMap:
    def __init__(self) -> None:
        self.array = [None]
        self.num_elems = 0
        self.load_factor = 0.75

    def __getitem__(self, key):
        search = self.linear_probe_search(key)

        if search != None:
            index, key, value = search
            return value

        return None

    def __setitem__(self, key, value) -> None:
        self.linear_probing(key, value)

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        while self.i < len(self.array) and self.array[self.i] == None:
            self.i += 1

        if self.i >= len(self.array):
            raise StopIteration

        ret_val = self.array[self.i]
        self.i += 1
        return ret_val

    def dynamic_resize(self):
        if (self.num_elems / len(self.array)) >= self.load_factor:
            self.table_double()

    def table_double(self) -> None:
        old_vals = [(key,val) for key,val in self]

        self.array = [None]*(len(self.array)*2)

        for key,val in old_vals:
            self.linear_probing(key,val)


    def get_hash_index(self, key) -> int:
        return hash(key) % len(self.array)

    def linear_probing(self, key, value):
        index = self.get_hash_index(key)

        while self.array[index] != None and self.array[index][0] != key:
            index = (index + 1) % len(self.array)

        if self.array[index] == None:
            self.num_elems += 1

        self.array[index] = (key, value)

        self.dynamic_resize()

    def linear_probe_search(self, key):
        index = self.get_hash_index(key)

        for i in range(index, index+len(self.array)):
            location_index = i % len(self.array)
            location = self.array[location_index]
            if location == None:
                return None

            if location[0] == key:
                return location_index, location[0], location[1]

    def delete(self, key):
        search = self.linear_probe_search(key)

        if search != None:
            index, key, value = search
            self.num_elems -= 1
            self.array[index] = self.find_replacement(index)

    def find_replacement(self, index):
        for i in range(index+1, index+len(self.array)):
            location_index = i % len(self.array)

            if self.array[location_index] == None:
                return None

            location_hash = hash(self.array[location_index][0]) % len(self.array)
            if location_hash <= index:
                replacer = self.array[location_index]
                self.array[location_index] = self.find_replacement(location_index)
                return replacer

    def __repr__(self) -> str:
        return str([x for x in self.array])

# type: ignore
def test():
    INSERT_ITEMS = 10000
    DELETE_ITEMS = INSERT_ITEMS // 10
    low_alpha = string.ascii_lowercase
    randint = random.randint

    insert_strings = list(set([
        (''.join([random.choice(low_alpha) for _ in range(randint(1,10))]))
    for _ in range(INSERT_ITEMS)]))


    insert_pairs = [(x, random.randint(0,1000)) for x in insert_strings]


    hashmap = HashMap()

    # Insert elements
    print(f"INSERTING {INSERT_ITEMS} elements")
    for key,val in insert_pairs:
        hashmap[key] = val

    # Assert insertions
    for key,val in insert_pairs:
        assert hashmap[key] == val

    # Delete some of them
    print(f'DELETING {DELETE_ITEMS} elements')
    for key,val in insert_pairs[:DELETE_ITEMS]:
        # print(hashmap)
        # print("DELETING", key,val, hashmap[key])
        hashmap.delete(key)

    # Assert deleted
    for key,val in insert_pairs[:DELETE_ITEMS]:
        # print(key,val, hashmap[key])
        assert hashmap[key] == None


    # Assert insertions still working
    print(f'RETESTING insertions')
    for key, val in insert_pairs[DELETE_ITEMS:]:
        # print(key, val, hashmap[key])
        # print(hash(key) % len(hashmap.array))
        assert hashmap[key] == val

    for key,val in hashmap:
        print(key,val)

if __name__ == "__main__":
    test()
