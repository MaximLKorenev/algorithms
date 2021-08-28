import LinkedList

a = LinkedList.LinkedList()
b = LinkedList.LinkedList()

a.add_in_tail(LinkedList.Node(1))
a.add_in_tail(LinkedList.Node(2))
a.add_in_tail(LinkedList.Node(3))
a.add_in_tail(LinkedList.Node(4))
a.add_in_tail(LinkedList.Node(5))

b.add_in_tail(LinkedList.Node(5))
b.add_in_tail(LinkedList.Node(4))
b.add_in_tail(LinkedList.Node(3))
b.add_in_tail(LinkedList.Node(2))
b.add_in_tail(LinkedList.Node(1))


def sum_link_list(first, second):
    if first.len() != second.len():
        return None
    c = LinkedList.LinkedList()
    n = first.len()
    a = first.head
    b = second.head
    for i in range(n):
        c.add_in_tail(LinkedList.Node(a.value + b.value))
        a = a.next
        b = b.next
    return c
