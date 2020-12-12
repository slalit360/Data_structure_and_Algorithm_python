# Data Structure	                            Time Complexity
#                       Average	                                    Worst
#                       Access	Search	Insertion	Deletion	    Access	Search	Insertion	Deletion
# Hash Table	        N/A	    Θ(1)	Θ(1)	    Θ(1)	        N/A	    O(n)	O(n)	    O(n)

# hashing key for index
# implement chaining to avoid collision on same hash
# 1.    chaining using Separate Chaining which uses Linked List of key and value for same index
#       [if we don't know no of element]
# 2.    chaining using linear probing (search next location)
#       [if we know finite no of element]
# usually have O(1) constant time complexity but on collision with same hash it can increase

class HashTableSeparateChaining:

    def __init__(self, size=10):
        self.MAX = size
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.MAX

    def add(self, key, value):
        hash = self.get_hash(key=key)
        found = False

        for idx, tup in enumerate(self.arr[hash]):
            if tup[0] == key:
                self.arr[hash][idx] = (key, value)
                found = True
                break

        if not found:
            self.arr[hash].append((key, value))

    def get(self, key):
        hash = self.get_hash(key=key)
        for tup in self.arr[hash]:
            if tup[0] == key:
                return tup[1]
        else:
            print(f"Key '{key}' not found in table")

    def delete(self, key):
        hash = self.get_hash(key=key)

        for tup in self.arr[hash]:
            if tup[0] == key:
                self.arr[hash].remove(tup)
                break
        else:
            print(f"Key '{key}' not found in table")
        # self.arr[hash] = []

    def __str__(self):
        op = ''
        for idx in range(self.MAX):
            tup_val = ''
            for tup in self.arr[idx]:
                tup_val += f"('{tup[0]}':{tup[1]}),"
            op += f'[{idx}] -> [{tup_val}]\n'
        return op

    __delitem__ = delete
    __setitem__ = add
    __getitem__ = get
    __repr__ = __str__


class HashTableLinearProbing:

    def __init__(self, size=10):
        self.MAX = size
        self.arr = [None for i in range(self.MAX)]

    def key_error(self, key): return f"Key '{key}' not found in table"

    def get_hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.MAX

    def add(self, key, value):
        hash = self.get_hash(key=key)
        if self.arr[hash] is None:
            self.arr[hash] = (key, value)
        else:
            new_hash = self.find_slot(key, hash)
            self.arr[new_hash] = (key, value)

    def get(self, key):
        hash = self.get_hash(key=key)
        if self.arr[hash] is None:
            return self.key_error(key)
        else:
            prob_idx = self.get_prob_range(hash)
            for idx in prob_idx:
                ele = self.arr[idx]
                if ele is None:
                    return self.key_error(key)
                elif ele[0] == key:
                    return ele[1]

    def delete(self, key):
        hash = self.get_hash(key=key)
        prob_idx = self.get_prob_range(hash)
        for idx in prob_idx:
            ele = self.arr[idx]
            if self.arr[idx] is None:
                return self.key_error(key)
            elif self.arr[idx][0] == key:
                self.arr[idx] = None
        else:
            return self.key_error(key)

    def get_prob_range(self, index):
        return list(range(index, self.MAX)) + list(range(0, index))

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for idx in prob_range:
            if self.arr[idx] is None:
                return idx
            if self.arr[idx][0] == key:
                return idx
        raise Exception("HASHMAP FULL")

    def __str__(self):
        op = ''
        for idx in range(self.MAX):
            op += f'[{idx}] -> {self.arr[idx]}\n'
        return op

    __delitem__ = delete
    __setitem__ = add
    __getitem__ = get
    __repr__ = __str__


if __name__ == '__main__':
    ht = HashTableLinearProbing(size=10)
    # ht.add('key 3', 'lalit')
    print("'key 3' : ", ht.get_hash('key 3'))
    ht['key 3'] = 11
    print("'345' : ", ht.get_hash('345'))
    ht['345'] = 12
    print("'453' : ", ht.get_hash('453'))
    ht['453'] = 13
    print("'def' : ", ht.get_hash('def'))
    ht['def'] = 14
    print("'dee' : ", ht.get_hash('dee'))
    ht['dee'] = 1222
    # ht['nrw'] = 12
    # ht['deef'] = 13
    # ht['desf'] = 14
    # ht['deae'] = 1222
    # print(ht.get(key='key 3'))
    print(ht)
    print(ht['def'])
    print(ht['deae'])
    del ht['dee']
    print(ht)
