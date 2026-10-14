# 2801. 统计范围内的步进数字数目
'''
给你两个正整数 low 和 high ，都用字符串表示，请你统计闭区间 [low, high] 内的 步进数字 数目。

如果一个整数相邻数位之间差的绝对值都 恰好 是 1 ，那么这个数字被称为 步进数字 。

请你返回一个整数，表示闭区间 [low, high] 之间步进数字的数目。

由于答案可能很大，请你将它对 109 + 7 取余 后返回。

注意：步进数字不能有前导 0 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
