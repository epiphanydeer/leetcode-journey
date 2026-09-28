# 1903. 字符串中的最大奇数
'''
给你一个字符串 num ，表示一个大整数。请你在字符串 num 的所有 非空子字符串 中找出 值最大的奇数 ，并以字符串形式返回。如果不存在奇数，则返回一个空字符串 "" 。

子字符串 是字符串中的一个连续的字符序列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
