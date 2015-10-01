def return_circular_node(self, head):
    """
    Given a circular linked list, implement an algorithm which returns the
    node at the beginning of the loop.
    """
    s1 = set()
    current = head
    while current:
        if current not in s1:
            s1.add(current)
        else:
            return current
        current = current.next
