class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0
        if v1 > v2:
            return 1

    def add(self, value):
        item = Node(value)

        if self.head is None:
            self.head = item
            self.tail = item
            return

        if (self.__ascending and self.compare(self.head.value, value) == 1) or (
              not self.__ascending and self.compare(self.tail.value, value) == -1):
            self.head.prev = item
            item.next = self.head
            self.head = item
            return

        if (self.__ascending and self.compare(self.tail.value, value) == -1) or (
              not self.__ascending and self.compare(self.tail.value, value) == 1):
            self.tail.next = item
            item.prev = self.tail
            self.tail = item
            return

        node = self.head
        while node is not None:
            if (self.__ascending and self.compare(node.next.value, value) == 1) or (
                not self.__ascending and self.compare(node.next.value, value) == -1):
                item.next = node.next
                item.prev = node
                node.next.prev = item
                node.next = item
                return
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            if (self.__ascending and self.compare(node.value, val) == 1) or (
              not self.__ascending and self.compare(node.value, val) == -1):
                break
            node = node.next
        return None

    def delete(self, val):
        node = self.head
        while node is not None:
            if (self.__ascending and self.compare(node.value, val) == 1) or (
                    not self.__ascending and self.compare(node.value, val) == -1):
                break
            if node is self.head:
                if node.value == val:
                    self.head = node.next
                    if self.head is None:
                        self.tail = None
                        return None
                    else:
                        self.head.prev = None
            if node.value == val:
                node.prev.next = node.next
                if node.next is None:
                    self.tail = node.prev
                    return
                else:
                    node.next.prev = node.prev
            node = node.next
        return None

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        size = 0
        node = self.head
        while node is not None:
            size += 1
            node = node.next
        return size

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = v1.strip()
        v2 = v2.strip()
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0
        if v1 > v2:
            return 1
