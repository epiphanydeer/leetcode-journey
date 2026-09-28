# 670. 最大交换
'''
给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
