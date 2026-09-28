# 2067. 等计数子串的数量
'''
给你一个下标从 0 开始的字符串 s，只包含小写英文字母和一个整数 count。如果 s 的子串中的每种字母在子串中恰好出现 count 次，这个子串就被称为等计数子串。

返回 s 中等计数子串的个数。

子串是字符串中连续的非空字符序列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def equalCountSubstrings(self, s, count):
        """
        :type s: str
        :type count: int
        :rtype: int
        """
        

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
