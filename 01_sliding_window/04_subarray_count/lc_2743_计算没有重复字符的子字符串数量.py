# 2743. 计算没有重复字符的子字符串数量
'''
给定你一个只包含小写英文字母的字符串 s。如果一个子字符串不包含任何字符至少出现两次（换句话说，它不包含重复字符），则称其为特殊子字符串。你的任务是计算特殊子字符串的数量。例如，在字符串 "pop" 中，子串 "po" 是一个特殊子字符串，然而 "pop" 不是特殊子字符串（因为 'p' 出现了两次）。

返回特殊子字符串的数量。

子字符串是指字符串中连续的字符序列。例如，"abc" 是 "abcd" 的一个子字符串，但 "acd" 不是。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def numberOfSpecialSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
