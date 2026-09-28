# 2457. 美丽整数的最小增量
'''
给你两个正整数 n 和 target 。

如果某个整数每一位上的数字相加小于或等于 target ，则认为这个整数是一个 美丽整数 。

找出并返回满足 n + x 是 美丽整数 的最小非负整数 x 。生成的输入保证总可以使 n 变成一个美丽整数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def makeIntegerBeautiful(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
