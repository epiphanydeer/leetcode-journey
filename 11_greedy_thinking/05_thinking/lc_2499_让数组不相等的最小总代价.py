# 2499. 让数组不相等的最小总代价
'''
给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，两者长度都为 n 。

每次操作中，你可以选择交换 nums1 中任意两个下标处的值。操作的 开销 为两个下标的 和 。

你的目标是对于所有的 0 <= i <= n - 1 ，都满足 nums1[i] != nums2[i] ，你可以进行 任意次 操作，请你返回达到这个目标的 最小 总代价。

请你返回让 nums1 和 nums2 满足上述条件的 最小总代价 ，如果无法达成目标，返回 -1 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimumTotalCost(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
