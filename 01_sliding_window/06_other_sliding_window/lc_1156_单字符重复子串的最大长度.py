# 1156. 单字符重复子串的最大长度
'''
如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。

给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
