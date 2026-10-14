# 10. 正则表达式匹配
'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

 '.' 匹配任意单个字符

 '*' 匹配零个或多个前面的那一个元素

返回一个布尔值，表示匹配是否覆盖整个输入字符串（而非部分）。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
