# 5. 最长回文子串
'''
给你一个字符串 s，找到 s 中最长的 回文 子串。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
