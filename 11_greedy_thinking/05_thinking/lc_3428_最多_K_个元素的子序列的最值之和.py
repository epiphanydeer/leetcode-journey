# 3428. 最多 K 个元素的子序列的最值之和
'''
给你一个整数数组 nums 和一个正整数 k，返回所有长度最多为 k 的 子序列 中 最大值 与 最小值 之和的总和。

非空子序列 是指从另一个数组中删除一些或不删除任何元素（且不改变剩余元素的顺序）得到的数组。

由于答案可能非常大，请返回对 109 + 7 取余数的结果。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minMaxSums(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
