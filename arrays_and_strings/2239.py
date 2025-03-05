# https://leetcode.com/problems/find-closest-number-to-zero/description/


class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = nums[0]

        for num in nums[1:]:
            if abs(num) < abs(res):
                res = num
            elif abs(num) == abs(res):
                res = max(num, res)

        return res
