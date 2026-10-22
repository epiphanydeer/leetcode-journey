# 350. 两个数组的交集 II
"""
给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。

"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
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
                ans.append(nums1[left])
                left += 1
                right += 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
