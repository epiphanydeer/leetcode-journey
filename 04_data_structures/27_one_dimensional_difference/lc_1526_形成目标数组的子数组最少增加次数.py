# 1526. 形成目标数组的子数组最少增加次数
'''
给你一个整数数组 target 和一个数组 initial ，initial 数组与 target  数组有同样的大小，且一开始全部为 0 。

一次操作中，你可以从 initial 数组中选择 任何 子数组，并将每个值加 1。

返回从 initial 数组构造 target 数组的最少操作次数。

答案保证在 32 位整数以内。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
