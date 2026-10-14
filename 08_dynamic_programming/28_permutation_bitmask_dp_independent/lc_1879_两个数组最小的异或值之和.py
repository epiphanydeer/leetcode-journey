# 1879. 两个数组最小的异或值之和
'''
给你两个整数数组 nums1 和 nums2 ，它们长度都为 n 。

两个数组的 异或值之和 为 (nums1[0] XOR nums2[0]) + (nums1[1] XOR nums2[1]) + ... + (nums1[n - 1] XOR nums2[n - 1]) （下标从 0 开始）。

 比方说，[1,2,3] 和 [3,2,1] 的 异或值之和 等于 (1 XOR 3) + (2 XOR 2) + (3 XOR 1) = 2 + 0 + 2 = 4 。

请你将 nums2 中的元素重新排列，使得 异或值之和 最小 。

请你返回重新排列之后的 异或值之和 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimumXORSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
