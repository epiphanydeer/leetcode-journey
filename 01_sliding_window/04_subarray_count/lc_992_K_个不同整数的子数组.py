# 992. K 个不同整数的子数组
'''
给定一个正整数数组 nums和一个整数 k，返回 nums 中 「好子数组」 的数目。

如果 nums 的某个子数组中不同整数的个数恰好为 k，则称 nums 的这个连续、不一定不同的子数组为 「好子数组 」。

 例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。

子数组 是数组的 连续 部分。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
