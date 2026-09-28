# 336. 回文对
'''
给定一个由唯一字符串构成的 0 索引 数组 words 。

回文对 是一对整数 (i, j) ，满足以下条件：

 0 <= i, j < words.length，

 i != j ，并且

 words[i] + words[j]（两个字符串的连接）是一个回文串。

返回一个数组，它包含 words 中所有满足 回文对 条件的字符串。

你必须设计一个时间复杂度为 O(sum of words[i].length) 的算法。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
