# 2165. 重排数字的最小值
'''
给你一个整数 num 。重排 num 中的各位数字，使其值 最小化 且不含 任何 前导零。

返回不含前导零且值最小的重排数字。

注意，重排各位数字后，num 的符号不会改变。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
