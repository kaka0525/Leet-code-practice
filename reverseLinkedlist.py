# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        Reverse a singly linked list
        For visualization: http://pythontutor.com/visualize.html#code=class+ListNode(object%29%3A%0D%0A++++def+__init__(self,+x%29%3A%0D%0A++++++++self.val+%3D+x%0D%0A++++++++self.next+%3D+None%0D%0A++++++++%0D%0A++++def+reverseList(self,+head%29%3A%0D%0A++++++++%22%22%22%0D%0A++++++++%3Atype+head%3A+ListNode%0D%0A++++++++%3Artype%3A+ListNode%0D%0A++++++++%22%22%22%0D%0A++++++++new_list+%3D+None%0D%0A++++++++current+%3D+head%0D%0A++++++++while+current%3A%0D%0A++++++++++++temp+%3D+new_list%0D%0A++++++++++++new_list+%3D+current%0D%0A++++++++++++current+%3D+current.next%0D%0A++++++++++++new_list.next+%3D+temp%0D%0A++++++++return+new_list%0D%0A%0D%0Anode1+%3D+ListNode(1%29%0D%0Anode2+%3D+ListNode(2%29%0D%0Anode3+%3D+ListNode(3%29%0D%0Anode4+%3D+ListNode(4%29%0D%0Anode1.next+%3D+node2%0D%0Anode2.next+%3D+node3%0D%0Anode3.next+%3D+node4%0D%0Anode1.reverseList(node1%29&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=2&rawInputLstJSON=%5B%5D&curInstr=25
        :type head: ListNode
        :rtype: ListNode
        """
        new_list = None
        current = head
        while current:
            temp = new_list
            new_list = current
            current = current.next
            new_list.next = temp
        return new_list
