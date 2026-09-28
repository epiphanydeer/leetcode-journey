# 2523. 范围内最接近的两个质数
'''
给你两个正整数 left 和 right ，请你找到两个整数 num1 和 num2 ，它们满足：

 left <= nums1 < nums2 <= right  。

 nums1 和 nums2 都是 质数 。

 nums2 - nums1 是满足上述条件的质数对中的 最小值 。

请你返回正整数数组 ans = [nums1, nums2] 。如果有多个整数对满足上述条件，请你返回 nums1 最小的质数对。如果不存在符合题意的质数对，请你返回 [-1, -1] 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
