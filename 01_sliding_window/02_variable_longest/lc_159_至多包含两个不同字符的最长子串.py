# 159. 至多包含两个不同字符的最长子串
'''
给你一个字符串 s，请你找出至多包含两个不同字符的最长子串，并返回该子串的长度。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
