# 2426. 满足不等式的数对数目
'''
给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，两个数组的大小都为 n ，同时给你一个整数 diff ，统计满足以下条件的 数对 (i, j) ：

 0 <= i < j <= n - 1 且

 nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff.

请你返回满足条件的 数对数目 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def numberOfPairs(self, nums1, nums2, diff):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type diff: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
