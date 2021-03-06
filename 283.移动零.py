#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return

        last_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_index], nums[i] = nums[i], nums[last_index]
                last_index += 1


# @lc code=end
