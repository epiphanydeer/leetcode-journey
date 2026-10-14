# 2809. 使数组和小于等于 x 的最少时间
'''
给你两个长度相等下标从 0 开始的整数数组 nums1 和 nums2 。每一秒，对于所有下标 0 <= i < nums1.length ，nums1[i] 的值都增加 nums2[i] 。操作 完成后 ，你可以进行如下操作：

 选择任一满足 0 <= i < nums1.length 的下标 i ，并使 nums1[i] = 0 。

同时给你一个整数 x 。

请你返回使 nums1 中所有元素之和 小于等于 x 所需要的 最少 时间，如果无法实现，那么返回 -1 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimumTime(self, nums1, nums2, x):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type x: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
