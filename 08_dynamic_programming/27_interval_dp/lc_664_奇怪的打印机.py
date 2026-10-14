# 664. 奇怪的打印机
'''
有台奇怪的打印机有以下两个特殊要求：

 打印机每次只能打印由 同一个字符 组成的序列。

 每次可以在从起始到结束的任意位置打印新字符，并且会覆盖掉原来已有的字符。

给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
