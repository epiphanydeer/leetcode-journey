# 1759. 统计同质子字符串的数目
'''
给你一个字符串 s ，返回 s 中 同质子字符串 的数目。由于答案可能很大，只需返回对 109 + 7 取余 后的结果。

同质字符串 的定义为：如果一个字符串中的所有字符都相同，那么该字符串就是同质字符串。

子字符串 是字符串中的一个连续字符序列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
