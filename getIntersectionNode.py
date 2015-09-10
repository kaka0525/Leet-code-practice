# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curr_a = headA
        curr_b = headB
        node_set = set()
        while curr_a:
            node_set.add(curr_a)
            curr_a = curr_a.next
        while curr_b:
            if curr_b not in node_set:
                node_set.add(curr_b)
                curr_b = curr_b.next
            else:
                return curr_b
        return None
