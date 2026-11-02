# 978. 最长湍流子数组
"""
给定一个整数数组 arr ，返回 arr 的 最大湍流子数组的长度 。

如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是 湍流子数组 。

更正式地来说，当 arr 的子数组 A[i], A[i+1], ..., A[j] 满足仅满足下列条件时，我们称其为湍流子数组：
【解题思路】
1. 总之就是找来回波动的数字，一会大一会小
2.
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        i = 0
        n = len(arr)
        ans = 0
        while i < n:
            start = i
            while i < n - 1 and (
                i == start
                and arr[i] != arr[i + 1]
                or i > start
                and ((arr[i - 1] - arr[i]) * (arr[i] - arr[i + 1]) < 0)
            ):
                i += 1
            ans = max(ans, i - start + 1)
            if i == start:
                i += 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxTurbulenceSize(arr=[9, 4, 2, 10, 7, 8, 8, 1, 9]))
