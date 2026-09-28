# 2514. 统计同位异构字符串数目
'''
给你一个字符串 s ，它包含一个或者多个单词。单词之间用单个空格 ' ' 隔开。

如果字符串 t 中第 i 个单词是 s 中第 i 个单词的一个 排列 ，那么我们称字符串 t 是字符串 s 的同位异构字符串。

 比方说，"acb dfe" 是 "abc def" 的同位异构字符串，但是 "def cab" 和 "adc bef" 不是。

请你返回 s 的同位异构字符串的数目，由于答案可能很大，请你将它对 109 + 7 取余 后返回。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countAnagrams(self, s):
        """
        :type s: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
