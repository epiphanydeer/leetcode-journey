"""
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
【解题思路】
1. 题目说了不考虑顺序，先排序，就可以双指针了
2.
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        left, right = 0, 0
        nums1.sort()
        nums2.sort()
        ans = []
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] > nums2[right]:
                right += 1
            else:
                if not ans or nums1[left] != ans[-1]:
                    ans.append(nums1[left])
                    left += 1
                    right += 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
