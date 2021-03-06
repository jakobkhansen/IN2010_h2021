# type: ignore
import string import random import hypothesis as hp from hypothesis import strategies as
st

# Hashmap implemented using open addressing
# Collisions are handled with linear probing


class HashMap:
    def __init__(self) -> None:
        self.array = [None]
        self.num_elems = 0
        self.load_factor = 0.75

    # Get value from key
    def __getitem__(self, key):
        search = self.linear_probe_search(key)

        if search != None:
            index, key, value = search
            return value

        return None

    # Insert / replace key
    def __setitem__(self, key, value) -> None:
        self.linear_probing(key, value)

    # Iterator, allows us to iterate over hashmap getting (key,value) every time
    def __iter__(self):
        for elem in self.array:
            if elem != None:
                yield elem

    # Allows us to use len(hashmap), gives number of elements in map
    def __len__(self):
        return self.num_elems

    # Resizes the table if necessary
    def dynamic_resize(self):
        if (self.num_elems / len(self.array)) >= self.load_factor:
            self.table_double()

    # Doubles size of table and inserts elements in new table
    def table_double(self) -> None:
        old_vals = [(key,val) for key,val in self]

        self.array = [None]*(len(self.array)*2)

        self.num_elems = 0

        for key,val in old_vals:
            self.linear_probing(key,val)


    # Gets the index where a key wants to be placed
    def get_hash_index(self, key) -> int:
        return hash(key) % len(self.array)

    # Linearly probes on an index until we find a spot where we can place key
    def linear_probing(self, key, value):
        index = self.get_hash_index(key)

        while self.array[index] != None and self.array[index][0] != key:
            index = (index + 1) % len(self.array)

        if self.array[index] == None:
            self.num_elems += 1

        self.array[index] = (key, value)

        # Resize table if necessary
        self.dynamic_resize()

    # Searches for a key and returns index, key and value if it is found. Else None
    def linear_probe_search(self, key):
        index = self.get_hash_index(key)

        for i in range(index, index+len(self.array)):
            location_index = i % len(self.array)
            location = self.array[location_index]
            if location == None:
                return None

            if location[0] == key:
                return location_index, location[0], location[1]

    # Deletes an element from the map using key
    # Deletes with 'hole-filling' strategy which finds a replacement
    # by searching ahead for a key which wants to be placed at or before the index
    # we are deleting. If we find no such element before we hit a None, we don't
    # need to fill the hole, because searching for any key after the hole does not
    # require us to 'pass' the hole.
    def delete(self, key):
        search = self.linear_probe_search(key)

        if search != None:
            index, key, value = search
            self.num_elems -= 1
            self.array[index] = None
            self.find_replacement(index)
            # self.array[index] = self.find_replacement(index)

    # Finds the replacement element, if we find a replacement, we need to fill the new
    # hole, recursively.
    def find_replacement(self, start):
        shift = 1
        i = start
        n = len(self.array)
        while self.array[(i+shift) % n] != None:
            shift_value = (i+shift) % n
            j = hash(self.array[shift_value][0]) % len(self.array)

            if not ((i < j <= i+shift) or (0 <= j <= i+shift - n)):
                self.array[i] = self.array[shift_value]
                self.array[shift_value] = None
                i = shift_value
                shift = 1
            else:
                shift += 1

    def __repr__(self) -> str:
        pairs = [f'{key}: {val}' for key,val in self]
        return '{' + ', '.join(pairs) + '}'

    def __str__(self) -> str:
        return self.__repr__()


@hp.given(st.dictionaries(st.integers(), st.text()))
@hp.settings(max_examples=1000)
def hyp_test(pairs):
    hashmap = HashMap()

    keys = list(pairs.keys())
    values = list(pairs.values())

    for key,val in pairs.items():
        hashmap[key] = val

    assert len(hashmap) == len(pairs)

    for key,val in pairs.items():
        assert hashmap[key] == val


    if len(hashmap) > 0:
        hashmap.delete(keys[0])

        assert hashmap[keys[0]] == None

if __name__ == "__main__":
    hyp_test()
