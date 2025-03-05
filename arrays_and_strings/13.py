# https://leetcode.com/problems/roman-to-integer/description/


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        num = 0
        prev_value = 0

        for c in s[::-1]:
            curr_value = symbol_table[c]

            if curr_value < prev_value:
                num -= curr_value
            else:
                num += curr_value

            prev_value = curr_value

        return num
