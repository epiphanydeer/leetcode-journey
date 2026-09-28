# 2311. 小于等于 K 的最长二进制子序列
'''
给你一个二进制字符串 s 和一个正整数 k 。

请你返回 s 的 最长 子序列的长度，且该子序列对应的 二进制 数字小于等于 k 。

注意：

 子序列可以有 前导 0 。

 空字符串视为 0 。

 子序列 是指从一个字符串中删除零个或者多个字符后，不改变顺序得到的剩余字符序列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
