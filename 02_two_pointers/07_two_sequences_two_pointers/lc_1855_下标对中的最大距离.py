# 1855. 下标对中的最大距离
"""
给你两个 非递增 的整数数组 nums1​​​​​​ 和 nums2​​​​​​ ，数组下标均 从 0 开始 计数。

下标对 (i, j) 中 0 <= i < nums1.length 且 0 <= j < nums2.length 。如果该下标对同时满足 i <= j 且 nums1[i] <= nums2[j] ，则称之为 有效 下标对，该下标对的 距离 为 j - i​​ 。​​

返回所有 有效 下标对 (i, j) 中的 最大距离 。如果不存在有效下标对，返回 0 。

一个数组 arr ，如果每个 1 <= i < arr.length 均有 arr[i-1] >= arr[i] 成立，那么该数组是一个 非递增 数组。
【解题思路】
1. 就是下标要小，数也要小，然后返回下标差
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
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        ans = 0
        left = 0
        for idx, x in enumerate(nums2):
            while left < len(nums1) and x - nums1[left] < 0:
                left += 1
            if left == len(nums1):
                break
            ans = max(ans, idx - left)
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDistance(nums1=[55, 30, 5, 4, 2], nums2=[100, 20, 10, 10, 5]))
