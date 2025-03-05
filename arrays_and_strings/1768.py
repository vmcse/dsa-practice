class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        res = ""

        m, n = len(word1), len(word2)
        max_size = max(m, n)

        for i in range(max_size):
            if i < m:
                res += word1[i]
            if i < n:
                res += word2[i]

        return res
