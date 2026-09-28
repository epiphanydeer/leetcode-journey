# 2645. 构造有效字符串的最少插入数
'''
给你一个字符串 word ，你可以向其中任何位置插入 "a"、"b" 或 "c" 任意次，返回使 word 有效 需要插入的最少字母数。

如果字符串可以由 "abc" 串联多次得到，则认为该字符串 有效 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def addMinimum(self, word):
        """
        :type word: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
