# 2193. 得到回文串的最少操作次数
'''
给你一个只包含小写英文字母的字符串 s 。

每一次 操作 ，你可以选择 s 中两个 相邻 的字符，并将它们交换。

请你返回将 s 变成回文串的 最少操作次数 。

注意 ，输入数据会确保 s 一定能变成一个回文串。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minMovesToMakePalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
