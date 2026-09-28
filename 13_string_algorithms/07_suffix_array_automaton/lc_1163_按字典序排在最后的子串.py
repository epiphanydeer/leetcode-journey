# 1163. 按字典序排在最后的子串
'''
给你一个字符串 s ，找出它的所有子串并按字典序排列，返回排在最后的那个子串。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
