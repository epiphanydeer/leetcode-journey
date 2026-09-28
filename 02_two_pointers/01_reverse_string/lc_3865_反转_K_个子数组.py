# 3865. 反转 K 个子数组
'''
给定一个长度为 n 的整数数组 nums 和一个整数 k。

你必须将数组划分为 k 个长度相等的连续子数组，并反转每个子数组。

保证 n 能被 k 整除。

返回上述操作后的结果数组。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def reverseSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
