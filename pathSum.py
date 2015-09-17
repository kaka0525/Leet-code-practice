# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        Given a binary tree and a sum, determine if the tree has a root-to-leaf
        path such that adding up all the values along the path equals the given
        sum.
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        for visualization: http://pythontutor.com/visualize.html#code=class+TreeNode(object%29%3A%0A++++def+__init__(self,+x%29%3A%0A++++++++self.val+%3D+x%0A++++++++self.left+%3D+None%0A++++++++self.right+%3D+None%0A%0A++++def+hasPathSum(self,+root,+sum%29%3A%0A++++++++%22%22%22%0A++++++++Given+a+binary+tree+and+a+sum,+determine+if+the+tree+has+a+root-to-leaf%0A++++++++path+such+that+adding+up+all+the+values+along+the+path+equals+the+given%0A++++++++sum.%0A++++++++%3Atype+root%3A+TreeNode%0A++++++++%3Atype+sum%3A+int%0A++++++++%3Artype%3A+bool%0A++++++++%22%22%22%0A++++++++if+root+is+None%3A%0A++++++++++++return+False%0A++++++++if+root.left+is+None+and+root.right+is+None%3A%0A++++++++++++return+root.val+%3D%3D+sum%0A++++++++sum+-%3D+root.val%0A++++++++return+self.hasPathSum(root.left,+sum%29+or+self.hasPathSum(root.right,+sum%29%0A%0Anode5+%3D+TreeNode(5%29%0Anode4+%3D+TreeNode(4%29%0Anode11+%3D+TreeNode(11%29%0Anode7+%3D+TreeNode(7%29%0Anode2+%3D+TreeNode(2%29%0Anode8+%3D+TreeNode(8%29%0Anode13+%3D+TreeNode(13%29%0Anode4+%3D+TreeNode(4%29%0Anode1+%3D+TreeNode(1%29%0A%0Anode5.left+%3D+node4%0Anode4.left+%3D+node11%0Anode11.left+%3D+node7%0Anode11.right+%3D+node2%0Anode5.right+%3D+node8%0Anode8.left+%3D+node13%0Anode8.right+%3D+node4%0Anode4.right+%3D+node1%0Anode5.hasPathSum(node5,22%29%0Anode5.hasPathSum(node5,17%29&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=2&rawInputLstJSON=%5B%5D&curInstr=0
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == sum
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
