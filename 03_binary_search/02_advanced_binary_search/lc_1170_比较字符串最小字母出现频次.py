# 1170. 比较字符串最小字母出现频次
'''
定义一个函数 f(s)，统计 s  中（按字典序比较）最小字母的出现频次 ，其中 s 是一个非空字符串。

例如，若 s = "dcce"，那么 f(s) = 2，因为字典序最小字母是 "c"，它出现了 2 次。

现在，给你两个字符串数组待查表 queries 和词汇表 words 。对于每次查询 queries[i] ，需统计 words 中满足 f(queries[i]) f(W) 的 词的数目 ，W 表示词汇表 words 中的每个词。

请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是第 i 次查询的结果。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
