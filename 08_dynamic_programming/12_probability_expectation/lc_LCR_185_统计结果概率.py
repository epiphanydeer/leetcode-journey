# LCR 185. 统计结果概率
'''
你选择掷出 num 个色子，请返回所有点数总和的概率。

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 num 个骰子所能掷出的点数集合中第 i 小的那个的概率。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def statisticsProbability(self, num):
        """
        :type num: int
        :rtype: List[float]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
