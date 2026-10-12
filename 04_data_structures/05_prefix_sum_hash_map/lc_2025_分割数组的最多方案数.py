# 2025. 分割数组的最多方案数
'''
给你一个下标从 0 开始且长度为 n 的整数数组 nums 。分割 数组 nums 的方案数定义为符合以下两个条件的 pivot 数目：

 1 <= pivot < n

 nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] + ... + nums[n - 1]

同时给你一个整数 k 。你可以将 nums 中 一个 元素变为 k 或 不改变 数组。

请你返回在 至多 改变一个元素的前提下，最多 有多少种方法 分割 nums 使得上述两个条件都满足。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def waysToPartition(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
