class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        find_list = []
        node = self.head
        while node is not None:
            if node.value == val:
                find_list.append(node)
            node = node.next
        return find_list

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node is self.head:
                if node.value == val:
                    self.head = node.next
                    if self.head is None:
                        self.tail = None
                        return
                    if all:
                        node = self.head
                        continue
                    else:
                        return
            prev = node
            node = node.next
            if node is None:
                self.tail = prev
                return
            if node.value == val:
                prev.next = node.next
                node = prev
                if not all:
                    return

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        size = 0
        node = self.head
        while node is not None:
            size += 1
            node = node.next
        return size

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            if newNode.next is None:
                self.tail = newNode
            return
        node = self.head
        while node is not None:
            if node.value == afterNode.value:
                newNode.next = node.next
                node.next = newNode
                if newNode.next is None:
                    self.tail = newNode
                return
            node = node.next
        return
