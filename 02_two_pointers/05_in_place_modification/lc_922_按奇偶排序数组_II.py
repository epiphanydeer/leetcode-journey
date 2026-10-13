# 922. 按奇偶排序数组 II
"""
给定一个非负整数数组 nums，  nums 中一半整数是 奇数 ，一半整数是 偶数 。

对数组进行排序，以便当 nums[i] 为奇数时，i 也是 奇数 ；当 nums[i] 为偶数时， i 也是 偶数 。

你可以返回 任何满足上述条件的数组作为答案 。
【解题思路】
1. 步长为2，俩指针分别对应奇数偶数
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, 1
        while left > len(nums):
            if nums[left] % 2 == 0:
                left += 2
            elif nums[right] % 2 != 0:
                right += 2
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 2
                right += 2
        return nums


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.sortArrayByParityII(nums=[4, 2, 5, 7]))
