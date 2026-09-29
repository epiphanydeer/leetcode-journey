# 658. 找到 K 个最接近的元素
"""
给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。
整数 a 比整数 b 更接近 x 需要满足：
 |a - x| < |b - x| 或者
 |a - x| == |b - x| 且 a < b
 【解题思路】
 1. 人话，找到跟x更相近的K个数字，用while维护这个K长的窗口
 2. 两段的指针开始判断距离谁更近，移动指针
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while left < right and (right - left + 1) > k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
            else:
                left += 1
        return arr[left : right + 1]


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3))
