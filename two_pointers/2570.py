# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/

# Using hashmap
from collections import defaultdict


class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        sums = defaultdict(lambda: 0)

        for id, num in nums1:
            sums[id] += num

        for id, num in nums2:
            sums[id] += num

        return [[id, sum] for id, sum in sorted(sums.items())]


# Using two pointers
class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        i, j = 0, 0
        m, n = len(nums1), len(nums2)

        while i < m and j < n:
            if nums1[i][0] == nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        while i < m:
            res.append(nums1[i])
            i += 1

        while j < n:
            res.append(nums2[j])
            j += 1

        return res
