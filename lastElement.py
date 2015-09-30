# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def find_length(self, head):
    """
    A helper function for the last_element to determine the length of the
    linked list
    """
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next
    return length


def last_element(self, head, k):
    """
    You have a linked list and want to find the kth to last node.
    """

    length = self.find_length(head)
    step_to_element = length - k
    current = head
    for element in xrange(step_to_element):
        current = current.next
    return current
