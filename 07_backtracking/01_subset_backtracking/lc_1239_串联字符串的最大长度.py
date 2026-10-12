# 1239. 串联字符串的最大长度
'''
给定一个字符串数组 arr，字符串 s 是将 arr 的含有 不同字母 的 子序列 字符串 连接 所得的字符串。

请返回所有可行解 s 中最长长度。

子序列 是一种可以从另一个数组派生而来的数组，通过删除某些元素或不删除元素而不改变其余元素的顺序。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
