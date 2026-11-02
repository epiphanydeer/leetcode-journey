# 845. 数组中的最长山脉
"""
把符合下列属性的数组 arr 称为 山脉数组 ：
 arr.length >= 3
 存在下标 i（0 < i < arr.length - 1），满足
 arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
 arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
给出一个整数数组 arr，返回最长山脉子数组的长度。如果不存在山脉子数组，返回 0 。
【解题思路】
1. 先判断是否上升，找上升的起点，确定山峰顶点，然后找下降直到不符合下降
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        i = 0
        n = len(arr)
        ans = 0
        while i < n - 2:
            # 先找上升段
            while i < n - 1 and arr[i] - arr[i + 1] >= 0:
                i += 1
            start = i
            # 找山顶
            while i < n - 1 and arr[i] - arr[i + 1] < 0:
                i += 1
            # 山顶不能平
            if i == start:
                continue
            peak = i
            # 找是否有下降
            while i < n - 1 and arr[i + 1] < arr[i]:
                i += 1
            if i > peak:
                ans = max(ans, i - start + 1)
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestMountain(arr=[2, 2, 2]))
    print(solution.longestMountain(arr=[2, 1, 4, 7, 3, 2, 5]))
