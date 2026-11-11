# 540. 有序数组中的单一元素
"""
给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。

请你找出并返回只出现一次的那个数。

你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。
【解题思路】
1. 因为成对，所以下标是偶奇成对，直到奇偶成对，说明有单一元素了
2. 只需要判断偶数和奇数下标的数字相等不，就确定他的位置
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) // 2
        while left < right:
            mid = (left + right) // 2
            if nums[mid * 2] == nums[mid * 2 + 1]:
                left = mid + 1
            else:
                right = mid
        return nums[left * 2]


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNonDuplicate(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8]))
    print(solution.singleNonDuplicate(nums=[3, 3, 7, 7, 10, 11, 11]))
