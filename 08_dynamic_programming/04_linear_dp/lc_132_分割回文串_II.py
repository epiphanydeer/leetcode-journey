# 132. 分割回文串 II
'''
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的 最少分割次数 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
