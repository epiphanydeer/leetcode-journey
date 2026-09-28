# 1100. 长度为 K 的无重复字符子串
'''
给你一个字符串 s，找出所有长度为 k 且不含重复字符的子串，请你返回全部满足要求的子串的数目。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def numKLenSubstrNoRepeats(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
