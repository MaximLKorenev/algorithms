class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return sum([ord(i) for i in value]) % self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        flag = False
        for i in range(self.size):
            if self.slots[i] is None:
                flag = True
                break
        if not flag:
            return None
        while flag:
            if self.slots[index] is None:
                return index
            index = (index + self.step) % self.size

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
            return index
        return None

    def find(self, value):
        index = self.hash_fun(value)
        for i in range(self.size):
            if self.slots[(index + i) % self.size] == value:
                return (index + i) % self.size
        return None
