# https://leetcode.com/problems/is-subsequence/description/


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True

        j = 0
        m, n = len(s), len(t)

        for i in range(n):
            if j < m and t[i] == s[j]:
                j += 1

        return j == len(s)
