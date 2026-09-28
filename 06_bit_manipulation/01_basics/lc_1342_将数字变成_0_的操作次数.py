# 1342. 将数字变成 0 的操作次数
'''
给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
