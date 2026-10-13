# 905. 按奇偶排序数组
"""
给你一个整数数组 nums，将 nums 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。

返回满足此条件的 任一数组 作为答案。
【解题思路】
1. 跟283一样，%2 == 0 的往前挪
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.sortArrayByParity(nums=[3, 1, 2, 4]))
