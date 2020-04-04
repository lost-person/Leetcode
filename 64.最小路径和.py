#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        m, n = len(grid), len(grid[0])

        res = [[0] * n for _ in range(m)]
        res[0][0] = grid[0][0]
        
        for i in range(1, m):
            res[i][0] = res[i - 1][0] + grid[i][0]
        
        for j in range(1, n):
            res[0][j] = res[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = min(res[i - 1][j], res[i][j - 1]) + grid[i][j]

        return res[m - 1][n - 1]
# @lc code=end

