# https://leetcode.com/problems/min-cost-climbing-stairs/description/


# Space = O(n)
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        def dp(step, memo):

            if step in memo:
                return memo[step]

            if step >= len(cost):
                return 0

            else:
                memo[step] = cost[step] + min(dp(step + 1, memo), dp(step + 2, memo))

            return memo[step]

        return min(dp(0, {}), dp(1, {}))


# Optimal, Space: O(1)
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        prev1 = prev2 = 0

        for i in range(len(cost)):
            curr_cost = cost[i] + min(prev1, prev2)

            prev1 = prev2
            prev2 = curr_cost

        return min(prev1, prev2)
