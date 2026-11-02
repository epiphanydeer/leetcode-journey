# 485. 最大连续 1 的个数
"""
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
【解题思路】
1.双指针，设置左边界，然后i+1去找符合条件的右边界
2. 按照题目要求，数组会被分割成若干组，每一组的判断/处理逻辑是相同的。
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        ans = 0
        while i < len(nums):
            if nums[i] != 1:
                i += 1
            start = i
            i += 1
            while i < len(nums) and nums[i]:
                i += 1
            ans = max(ans, i - start)
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0, 1]))
