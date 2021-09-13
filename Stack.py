class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.stack:
            return self.stack.pop(-1)
        return None

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None
