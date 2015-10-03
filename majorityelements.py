class Solution(object):

    def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        Given an array of size n, find the majority element. The majority
        element is the element that appears more than ⌊ n/2 ⌋ times.
        You may assume that the array is non-empty and the majority element
        always exist in the array.
        """
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        return max(d, key=d.get)
