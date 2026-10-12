# 1542. 找出最长的超赞子字符串
'''
给你一个字符串 s 。请返回 s 中最长的 超赞子字符串 的长度。

「超赞子字符串」需满足满足下述两个条件：

 该字符串是 s 的一个非空子字符串

 进行任意次数的字符交换后，该字符串可以变成一个回文字符串
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def longestAwesome(self, s):
        """
        :type s: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
