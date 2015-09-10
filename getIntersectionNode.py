# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        Write a program to find the node at which the intersection of two
        singly linked lists begins.
        :type head1, head1: ListNode
        :rtype: ListNode
        For visualization http://pythontutor.com/visualize.html#code=class+ListNode(object%29%3A%0D%0A++++def+__init__(self,+x%29%3A%0D%0A++++++++self.val+%3D+x%0D%0A++++++++self.next+%3D+None%0D%0A++++++++%0D%0A++++def+getIntersectionNode(self,+headA,+headB%29%3A%0D%0A++++++++%22%22%22%0D%0A++++++++%3Atype+head1,+head1%3A+ListNode%0D%0A++++++++%3Artype%3A+ListNode%0D%0A++++++++%22%22%22%0D%0A++++++++current_a+%3D+headA%0D%0A++++++++while+current_a%3A%0D%0A++++++++++++current_b+%3D+headB%0D%0A++++++++++++while+current_b%3A%0D%0A++++++++++++++++if+current_a+is+current_b%3A%0D%0A++++++++++++++++++++return+current_b%0D%0A++++++++++++++++else%3A%0D%0A++++++++++++++++++++current_b+%3D+current_b.next%0D%0A++++++++++++current_a+%3D+current_a.next%0D%0A%0D%0Anode1+%3D+ListNode(1%29%0D%0Anode2+%3D+ListNode(2%29%0D%0Anode3+%3D+ListNode(3%29%0D%0Anode4+%3D+ListNode(4%29%0D%0Anode5+%3D+ListNode(5%29%0D%0Anode6+%3D+ListNode(6%29%0D%0Anode7+%3D+ListNode(7%29%0D%0Anode8+%3D+ListNode(8%29%0D%0A%0D%0Anode1.next+%3D+node2%0D%0Anode2.next+%3D+node3%0D%0Anode3.next+%3D+node4%0D%0Anode5.next+%3D+node6%0D%0Anode6.next+%3D+node7%0D%0Anode7.next+%3D+node8%0D%0Anode8.next+%3D+node4%0D%0A%0D%0A%0D%0A%0D%0Anode1.getIntersectionNode(node1,node5%29&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=2&rawInputLstJSON=%5B%5D&curInstr=0
        """
        current_a = headA
        while current_a:
            current_b = headB
            while current_b:
                if current_a is current_b:
                    return current_b
                else:
                    current_b = current_b.next
            current_a = current_a.next
