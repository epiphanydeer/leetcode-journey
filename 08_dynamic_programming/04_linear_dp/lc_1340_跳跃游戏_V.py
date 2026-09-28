# 1340. 跳跃游戏 V
'''
给你一个整数数组 arr 和一个整数 d 。每一步你可以从下标 i 跳到：

 i + x ，其中 i + x < arr.length 且 0 < x <= d 。

 i - x ，其中 i - x >= 0 且 0 < x <= d 。

除此以外，你从下标 i 跳到下标 j 需要满足：arr[i] > arr[j] 且 arr[i] > arr[k] ，其中下标 k 是所有 i 到 j 之间的数字（更正式的，min(i, j) < k < max(i, j)）。

你可以选择数组的任意下标开始跳跃。请你返回你 最多 可以访问多少个下标。

请注意，任何时刻你都不能跳到数组的外面。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
