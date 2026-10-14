# 456. 132 模式
'''
给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，并同时满足：i 和 nums[i] 。

如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
