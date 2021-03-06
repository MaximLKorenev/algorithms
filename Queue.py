class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if self.queue:
            return self.queue.pop()
        return None

    def size(self):
        return len(self.queue)