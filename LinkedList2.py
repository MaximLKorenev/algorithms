class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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
                        return None
                    else:
                        self.head.prev = None
                    if all:
                        node = self.head
                        continue
                    else:
                        return

            if node.value == val:
                node.prev.next = node.next
                if node.next is None:
                    self.tail = node.prev
                    return
                else:
                    node.next.prev = node.prev
                if not all:
                    return
            node = node.next
        return None

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
        node = self.head
        if afterNode is None:
            if node:
                self.add_in_tail(newNode)
            else:
                self.add_in_head(newNode)
            return

        while node is not None:
            if node.value == afterNode.value:
                newNode.next = node.next
                newNode.prev = node
                node.next = newNode

                if newNode.next is None:
                    self.tail = newNode
                else:
                    newNode.next.prev = newNode
                return
            node = node.next
        return

    def add_in_head(self, newNode):
        if self.head is None:
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode
