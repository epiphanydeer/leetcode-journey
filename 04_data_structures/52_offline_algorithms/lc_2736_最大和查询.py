# 2736. 最大和查询
'''
给你两个长度为 n 、下标从 0 开始的整数数组 nums1 和 nums2 ，另给你一个下标从 1 开始的二维数组 queries ，其中 queries[i] = [xi, yi] 。

对于第 i 个查询，在所有满足 nums1[j] >= xi 且 nums2[j] >= yi 的下标 j (0 <= j < n) 中，找出 nums1[j] + nums2[j] 的 最大值 ，如果不存在满足条件的 j 则返回 -1 。

返回数组 answer ，其中 answer[i] 是第 i 个查询的答案。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maximumSumQueries(self, nums1, nums2, queries):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
