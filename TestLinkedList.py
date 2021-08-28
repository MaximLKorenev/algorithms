import unittest
from LinkedList import LinkedList, Node


class LinkedListTests(unittest.TestCase):
    def test_del_empty_list(self):
        s = LinkedList()
        self.assertEqual(s.delete(5), None)

    def test_del_single_node(self):
        m = Node(5)
        s = LinkedList()
        s.add_in_tail(m)
        s.delete(5)
        self.assertEqual(s.head, None)

    def test_del_many_node(self):
        s = [Node(1) for _ in range(1000000)]
        a = LinkedList()
        a.add_in_tail(Node(5))
        for x in s:
            a.add_in_tail(x)
        a.add_in_tail(Node(6))
        a.delete(1, all=True)
        self.assertEqual(a.head.value, 5)
        self.assertEqual(a.tail.value, 6)

    def test_find_all_empty_list(self):
        s = LinkedList()
        self.assertEqual(s.find_all(5), [])

    def test_find_all_single_node(self):
        m = Node(5)
        s = LinkedList()
        s.add_in_tail(m)
        self.assertEqual(s.find_all(5), [m])

    def test_find_all_many_node(self):
        m = [Node(5) for _ in range(100000)]
        s = LinkedList()
        for x in m:
            s.add_in_tail(x)
        self.assertEqual(s.find_all(5), m)

    def test_clean(self):
        m = [Node(5) for _ in range(100000)]
        s = LinkedList()
        for x in m:
            s.add_in_tail(x)
        s.clean()
        self.assertEqual(s.head, None)
        self.assertEqual(s.tail, None)

    def test_len_empty_list(self):
        s = LinkedList()
        self.assertEqual(s.len(), 0)

    def test_len_many_node(self):
        m = [Node(5) for _ in range(100000)]
        s = LinkedList()
        for x in m:
            s.add_in_tail(x)
        self.assertEqual(s.len(), 100000)

    def test_insert_first_in_empty_list(self):
        m = Node(5)
        s = LinkedList()
        s.insert(None, m)
        self.assertEqual(s.head, m)
        self.assertEqual(s.tail, m)

    def test_insert_first(self):
        m = Node(5)
        n = Node(3)
        s = LinkedList()
        s.add_in_tail(n)
        s.insert(None, m)
        self.assertEqual(s.head, m)
        self.assertEqual(s.tail, n)

    def test_insert_after_node(self):
        m = Node(5)
        n = Node(3)
        s = LinkedList()
        s.add_in_tail(n)
        s.insert(n, m)
        self.assertEqual(s.head, n)
        self.assertEqual(s.tail, m)




if __name__ == '__main__':
    unittest.main()
