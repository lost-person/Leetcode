#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1: return 0

        max_k = 2
        n = len(prices)
        dp = [[[0, 0] for _ in range(max_k + 1)] for _ in range(n)]

        for i in range(n):
            for k in range(max_k, 0, -1):
                if not i:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1],
                                  dp[i - 1][k - 1][0] - prices[i])

        return dp[n - 1][max_k][0]


# @lc code=end
