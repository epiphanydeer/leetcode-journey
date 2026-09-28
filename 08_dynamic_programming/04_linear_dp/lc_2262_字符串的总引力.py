# 2262. 字符串的总引力
'''
字符串的 引力 定义为：字符串中 不同 字符的数量。

 例如，"abbca" 的引力为 3 ，因为其中有 3 个不同字符 'a'、'b' 和 'c' 。

给你一个字符串 s ，返回 其所有子字符串的总引力 。

子字符串 定义为：字符串中的一个连续字符序列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
