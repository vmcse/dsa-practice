# https://leetcode.com/problems/sort-array-by-parity/


# Brute force
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even_nums = [num for num in nums if num % 2 == 0]
        odd_nums = [num for num in nums if num % 2 != 0]

        return even_nums + odd_nums


# Two Pointers
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1

        while l < r:
            is_left_even = nums[l] % 2 == 0
            is_right_even = nums[r] % 2 == 0

            if not is_left_even:
                if is_right_even:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                r -= 1

            elif is_left_even:
                if not is_right_even:
                    r -= 1
                l += 1

        return nums
