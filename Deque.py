class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.insert(0, item)

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.deque:
            return self.deque.pop(0)
        return None

    def removeTail(self):
        if self.deque:
            return self.deque.pop()
        return None

    def size(self):
        return len(self.deque)
