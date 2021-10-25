class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        return sum([ord(i) for i in key]) % self.size

    def is_key(self, key):
        start_index = self.hash_fun(key)
        for i in range(self.size):
            if self.slots[(start_index + i) % self.size] == key:
                return True
        return False

    def put(self, key, value):
        index = self.hash_fun(key)
        x = 2
        if self.is_key(key):
            while self.slots[index] != key:
                index = (index + x * x) % self.size
                x += 1
            self.values[index] = value
        else:
            while self.slots[index] is not None:
                index = (index + x * x) % self.size
                x += 1
            self.slots[index] = key
            self.values[index] = value

    def get(self, key):
        if self.is_key(key):
            index = self.hash_fun(key)
            x = 2
            while self.slots[index] != key:
                index = (index + x * x) % self.size
                x += 1
            return self.values[index]
        else:
            return None
