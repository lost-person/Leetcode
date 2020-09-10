#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n # initialize left as the leftmost boundary possible
        right = [n] * n # initialize right as the rightmost boundary possible
        height = [0] * n

        maxarea = 0

        for i in range(m):

            cur_left, cur_right = 0, n
            # update height
            for j in range(n):
                if matrix[i][j] == '1': height[j] += 1
                else: height[j] = 0
            # update left
            for j in range(n):
                if matrix[i][j] == '1': left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update right
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1': right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # update the area
            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))

        return maxarea

        # # 位运算，太强了
        # m, n = len(matrix), len(matrix[0])
        # # 转换为 int
        # nums = [int(''.join(row), base=2) for row in matrix]
        # ans, N = 0, len(nums)
        # for i in range(N):
        #     j, num = i, nums[i]
        #     while j < N:
        #         num = num & nums[j]
        #         if not num:
        #             break
        #         l, curnum = 0, num
        #         # 通过左移计算有效宽度
        #         while curnum:
        #             l += 1
        #             curnum = curnum & (curnum << 1)
        #         ans = max(ans, l * (j - i + 1))
        #         j += 1
        # return ans

        # Get the maximum area in a histogram given its heights
        # def leetcode84(heights):
        #     stack = [-1]

        #     maxarea = 0
        #     for i in range(len(heights)):

        #         while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
        #             maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
        #         stack.append(i)

        #     while stack[-1] != -1:
        #         maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        #     return maxarea

        # maxarea = 0
        # dp = [0] * len(matrix[0])
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):

        #         # update the state of this row's histogram using the last row's histogram
        #         # by keeping track of the number of consecutive ones

        #         dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0

        #     # update maxarea with the maximum area from this row's histogram
        #     maxarea = max(maxarea, self.leetcode84(dp))
        # return maxarea

# @lc code=end

