# 340. 至多包含 K 个不同字符的最长子串
'''
给你一个字符串 s 和一个整数 k，请你找出至多包含 k 个不同字符的最长子串，并返回该子串的长度。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
