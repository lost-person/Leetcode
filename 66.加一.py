#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # return list(map(int, list(str(int(''.join(map(str, digits))) + 1))))
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break

        if digits[0] == 0:
            digits.insert(0, 1)

        return digits


# @lc code=end
