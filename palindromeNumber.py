class Solution(object):
    def isPalindrome(self, x):
        """
        Determine whether an integer is a palindrome. Do this without
        extra space.
        :type x: int
        :rtype: bool
                """
        num = str(x)
        count = 0
        for i in num:
            if num[count] == num[-1 - (count)]:
                count += 1
            else:
                return False
        return True
