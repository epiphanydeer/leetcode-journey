# 943. 最短超级串
'''
给定一个字符串数组 words，找到以 words 中每个字符串作为子字符串的最短字符串。如果有多个有效最短字符串满足题目条件，返回其中 任意一个 即可。

我们可以假设 words 中没有字符串是 words 中另一个字符串的子字符串。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def shortestSuperstring(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
