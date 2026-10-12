# 2586. 统计范围内的元音字符串数
'''
给你一个下标从 0 开始的字符串数组 words 和两个整数：left 和 right 。

如果字符串以元音字母开头并以元音字母结尾，那么该字符串就是一个 元音字符串 ，其中元音字母是 'a'、'e'、'i'、'o'、'u' 。

返回 words[i] 是元音字符串的数目，其中 i 在闭区间 [left, right] 内。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
