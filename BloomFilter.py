class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bitmask = 1 << f_len

    def hash1(self, str1):
        ind = 0
        for c in str1:
            code = ord(c)
            ind = ((ind * 17) + code) % self.filter_len
        return 1 << ind

    def hash2(self, str1):
        ind = 0
        for c in str1:
            code = ord(c)
            ind = ((ind * 223) + code) % self.filter_len
        return 1 << ind

    def add(self, str1):
        mask = self.hash1(str1) | self.hash2(str1)
        self.bitmask |= mask

    def is_value(self, str1):
        mask = self.hash1(str1) | self.hash2(str1)
        return (self.bitmask & mask) == mask
