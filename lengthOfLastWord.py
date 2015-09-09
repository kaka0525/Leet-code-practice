class Solution(object):
    def lengthOfLastWord(self, s):
        """
        Given a string s consists of upper/lower-case alphabets and empty space
        characters ' ', return the length of last word in the string.
        If the last word does not exist, return 0.
        :type s: str
        :rtype: int
        """
        current = s.split()
        if len(current) == 0:
            return 0
        else:
            return len(current[-1])
