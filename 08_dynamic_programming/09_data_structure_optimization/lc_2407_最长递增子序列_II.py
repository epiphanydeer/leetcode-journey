# 2407. 最长递增子序列 II
'''
给你一个整数数组 nums 和一个整数 k 。

找到 nums 中满足以下要求的最长子序列：

 子序列 严格递增

 子序列中相邻元素的差值 不超过 k 。

请你返回满足上述要求的 最长子序列 的长度。

子序列 是从一个数组中删除部分元素后，剩余元素不改变顺序得到的数组。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def lengthOfLIS(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
