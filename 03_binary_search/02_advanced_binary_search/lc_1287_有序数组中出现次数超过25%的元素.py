# 1287. 有序数组中出现次数超过25%的元素
"""
给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。

请你找到并返回这个整数
【解题思路】
1. 分块，分节点，超过25%，也就是看节点上的数字是否出现在下一个节点上
2. 既可以多次二分，也可以直接判断是否在下一个节点上
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def lower_bound(self, arr: list[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        threshold = n // 4
        candidate = [arr[n // 4], arr[n // 2], arr[3 * n // 4]]
        for i in candidate:
            left = self.lower_bound(arr, i)
            right = self.lower_bound(arr, i + 1) - 1
            if right - left >= threshold:
                return i
        return arr[0]


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.findSpecialInteger(arr=[1, 2, 2, 2, 2, 2, 2, 6, 6, 6, 6, 7, 10]))
    print(solution.findSpecialInteger(arr=[1]))
